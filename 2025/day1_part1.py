dialer = 50

password = 0

with open("day1_input.txt", "r") as input_file:
    for rotation in input_file.readlines():
        direction = rotation[0]
        offset = int(rotation[1:])

        if direction == "R":
            dialer += offset
        else:
            dialer -= offset

        dialer %= 100
        password += dialer == 0

print(password)