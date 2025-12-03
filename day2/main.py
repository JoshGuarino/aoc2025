def load_input():
    id_ranges = []
    with open("input.txt") as file:
        input = file.read()
        lines = input.split(",")
        for line in lines:
            range = line.split("-")
            id_ranges.append((int(range[0]), int(range[1])))
    return id_ranges 

def check_id_valid1(id: int) -> bool:
    string_id = str(id)
    length = len(string_id)

    # Check if the length is odd, odd numbers can't be palindromes
    # meaning they don't fit the criteria for an invalid id
    if length % 2 != 0:
        return True 
    
    # Split the string into two halves
    mid = length // 2
    first_half = string_id[:mid]
    second_half = string_id[mid:]

    # Check if the first half is a palindrome
    # invalid ids should be the same
    # based on the criteria for an invalid id
    return first_half != second_half

def check_id_valid2(id: int) -> bool:
    string_id = str(id)
    length = len(string_id)

    # An ID is invalid if it is made of a repeating sequence of digits
    # The length of the sequence can be from 1 to half the length of the ID
    for i in range(1, length // 2 + 1):
        # The length of the ID must be a multiple of the sequence length
        if length % i == 0:
            sequence = string_id[:i]
            repetitions = length // i
            if sequence * repetitions == string_id:
                # Found a repeating sequence, so the ID is invalid
                return False
    
    # No repeating sequence found, so the ID is valid
    return True 

def main():
    id_ranges = load_input()
    invalid_ids1 = []
    invalid_ids2 = []
    for id_range in id_ranges:
        for i in range(id_range[0], id_range[1]):
            if not check_id_valid1(i):
                invalid_ids1.append(i)
            if not check_id_valid2(i):
                invalid_ids2.append(i)

    return sum(invalid_ids1), sum(invalid_ids2)

if __name__ == "__main__":
    answer = main()
    print(answer)
