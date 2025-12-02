def main():
    dial = 50 # represents what the dial is currently at
    rotations = [] # stores the rotations
    zeros = 0 # how many times the dial was at zero

    # load input into a list of dictionaries
    with open("input.txt") as file:
        for rotation in file:
            rotations.append({"direction": rotation[0], "distance": int(rotation[1:])})

    # rotate the dial
    for rotation in rotations:
        # normalize the distance to be between 0 and 100 as 
        # numbers bigger than 100 will just wrap around
        normalized_distance = rotation["distance"] % 100 

        # rotate the dial right
        if rotation["direction"] == "R":
            dial += normalized_distance
            dial -= 100 if dial > 100 else 0
            dial = 0 if dial == 100 else dial # 100 means the dial wrapped around to 0

        # rotate the dial left
        elif rotation["direction"] == "L":
            dial -= normalized_distance
            dial += 100 if dial < 0 else 0

        # if the dial is at zero, increment the zeros counter
        if dial == 0:
            zeros += 1

    return zeros

if __name__ == "__main__":
    answer = main()
    print(answer)
