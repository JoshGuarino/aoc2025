def load_input():
    with open("input.txt") as file:
        input = file.read()
        lines = input.splitlines()
        banks = [[int(i) for i in line] for line in lines]
    return banks

def part1(banks: list[list[int]]) -> int:
    joltages = []
    for bank in  banks:
        max_val = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                val = int(f"{bank[i]}{bank[j]}")
                if val > max_val:
                    max_val = val
        
        joltages.append(max_val)
    
    return sum(joltages) 

def part2(banks: list[list[int]]) -> int:
    TARGET_LENGTH = 12
    joltages = []

    for bank in banks:
        # Number of digits to remove (drop)
        k = len(bank) - TARGET_LENGTH
        
        # 'result' will store the digits we select, forming the largest number
        result = []
        
        for digit in bank:
            # Greedy step: While we have drops left (k > 0), and the result is 
            # not empty, AND the current digit is greater than the last digit 
            # in our result, we drop the last digit from the result.
            while k > 0 and result and digit > result[-1]:
                result.pop()
                k -= 1
            
            # Add the current digit to the result list
            result.append(digit)
            
        # If we still have drops left after iterating through all digits, 
        # it means the smallest digits were at the end. Trim the result list.
        # Note: Since the bank length is 15 and TARGET_LENGTH is 12, 
        # this trimming is equivalent to just taking the first TARGET_LENGTH elements.
        final_digits = result[:TARGET_LENGTH]
        
        joltage_str = "".join(map(str, final_digits))
        joltages.append(int(joltage_str))

    return sum(joltages)
  

def main():
    banks = load_input()
    part1_answer = part1(banks)
    part2_answer = part2(banks)

    return part1_answer, part2_answer

if __name__ == "__main__":
    answer = main()
    print(answer)
