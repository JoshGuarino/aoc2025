from os import wait


def load_input():
    id_ranges = []
    with open("input.txt") as file:
        input = file.read()
        lines = input.split(",")
        for line in lines:
            range = line.split("-")
            id_ranges.append((int(range[0]), int(range[1])))

    return id_ranges 

def check_id_valid(id: int) -> bool:
    string_id = str(id)
    length = len(string_id)

    # Check if the length is odd, 
    # odd numbers can't be palindromes
    # meaning they don't fit the criteria
    # for and invalid id
    if length % 2 != 0:
        return True 
    
    # Split the string into two halves
    mid = length // 2
    first_half = string_id[:mid]
    second_half = string_id[mid:]

    # Check if the first half is a palindrome
    # invlid ids should be the same
    # based on the criteria for an invalid id
    return first_half != second_half

def part1(id_ranges: list):
    invalid_ids = []

    # Check every id in the range
    for id_range in id_ranges:
        for i in range(id_range[0], id_range[1]):
            if not check_id_valid(i):
                invalid_ids.append(i)

    # Sum the invalid ids
    return sum(invalid_ids)

def main():
    id_ranges = load_input()
    sum1 = part1(id_ranges)

    return sum1 

if __name__ == "__main__":
    answer = main()
    print(answer)
