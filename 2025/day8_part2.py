import math

class DSU:
    def __init__(self, points):
        self._points = points
        self._parents = list(range(len(points)))
        self._size = [1] * len(points)

    def find_parent(self, pt):
        parent = self._parents[pt]

        if parent == pt: return parent

        self._parents[pt] = self.find_parent(parent)
        return self._parents[pt]

    def get_remaining_individual_points(self):
        remaining = []
        for i in range(len(self._points)):
            if self.find_parent(i) == i: remaining.append(self._points[i])
        return remaining

    def union(self, point_a, point_b):
        parent_of_a = self.find_parent(point_a)
        parent_of_b = self.find_parent(point_b)

        if parent_of_a == parent_of_b: return False

        size_of_parent_of_a = self._size[parent_of_a]
        size_of_parent_of_b = self._size[parent_of_b]

        if size_of_parent_of_a <= size_of_parent_of_b:
            self._parents[parent_of_a] = parent_of_b
            self._size[parent_of_b] += size_of_parent_of_a
            return True

        self._parents[parent_of_b] = parent_of_a 
        self._size[parent_of_a] += size_of_parent_of_b
        return True

def get_euclidean_dist(point_a, point_b):
    return math.sqrt(
        sum(
            [ (p2-p1) ** 2 for p1,p2 in zip(point_a, point_b) ]
        )
    )

with open("day8_input.txt", "r") as input_file:
    points = []
    for line in input_file.readlines():
        points.append(tuple(map(int, line.strip().split(","))))


    points_and_distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            point1 = points[i]
            point2 = points[j]
            d = get_euclidean_dist(point1, point2)

            points_and_distances.append([d, (i, j)])

    points_and_distances.sort(key=lambda x: x[0])

    dsu = DSU(points)

    final_points = []
    for entry in points_and_distances:
        pt_a, pt_b = entry[1]

        dsu.union(pt_a, pt_b)

        rem_after_union = dsu.get_remaining_individual_points()
        if len(rem_after_union) == 1:
            final_points.append(points[pt_a])
            final_points.append(points[pt_b])
    
    print(final_points[0][0] * final_points[1][0])
