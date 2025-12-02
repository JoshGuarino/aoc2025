def main() -> tuple[int, int]:
    rotations = [] # stores the rotations

    # load input into a list of dictionaries
    with open("input.txt") as file:
        for rotation in file:
            rotations.append({"direction": rotation[0], "distance": int(rotation[1:])})

    return part1(rotations), part2(rotations)

def part1(rotations: list) -> int:
    zeros = 0
    dial = 50

    # rotate the dial
    for rotation in rotations:
        direction = rotation["direction"]
        distance = rotation["distance"]

        # normalize the distance to be between 0 and 100 as 
        # numbers bigger than 100 will just wrap around
        remainder = distance % 100 

        if direction == "R":
            dial += remainder 
            dial -= 100 if dial > 100 else 0
            dial = 0 if dial == 100 else dial # 100 means the dial wrapped around to 0
        elif direction == "L":
            dial -= remainder 
            dial += 100 if dial < 0 else 0

        # increment the counter if the dial is at 0
        if dial == 0:
            zeros += 1

    return zeros

    
def part2(rotations: list) -> int:
    zeros = 0
    dial = 50

    for rotation in rotations:
        distance = rotation["distance"]
        direction = rotation["direction"]

        # Count full circles, Every 100 clicks is a full circle, 
        # guaranteeing we hit 0 once per circle
        zeros += distance // 100

        remainder = distance % 100

        if direction == "R":
            # If moving Right (adding), we cross 0 if we go past 99.
            # In modulo arithmetic, 0 is equivalent to 100.
            if dial + remainder >= 100:
                zeros += 1
            
            # Update position
            dial = (dial + remainder) % 100

        elif direction == "L":
            # If moving Left (subtracting), we cross 0 if we go 0 or below.
            # Crucial Check: We only count if we were strictly POSITIVE before.
            # If we started at 0 and moved Left immediately, we are moving AWAY 
            # from 0, so we don't count that as a "hit".
            if dial > 0 and (dial - remainder) <= 0:
                zeros += 1
            
            # Update position
            dial = (dial - remainder) % 100

    return zeros

if __name__ == "__main__":
    answer = main()
    print(answer)
