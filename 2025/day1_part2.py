dialer = 50

password = 0

with open("day1_input.txt", "r") as input_file:
    for rotation in input_file.readlines():
        direction = rotation[0]
        offset = int(rotation[1:])

        if offset >= 100:  # If offset is more than 100, we would atleast complete 1 full cycle 
            password += offset // 100  # Normalize offset by adding total cycles i.e offset//100 to our result 
            offset %= 100  # keep the remainder only

        if offset == 0: continue

        was_dialer_at_zero = dialer == 0
        dialer += offset if direction == "R" else -offset
        
        if (
            dialer >= 100 
            or dialer == 0
            or (dialer < 0 and not was_dialer_at_zero)
        ): 
            password += 1

        dialer %= 100

print(password)