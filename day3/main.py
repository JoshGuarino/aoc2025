def load_input():
    with open("input.txt") as file:
        input = file.read()
        lines = input.splitlines()
        banks = [[int(i) for i in line] for line in lines]
    return banks

def main():
    joltages = []
    banks = load_input()
    for bank in  banks:
        max_val = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                val = int(f"{bank[i]}{bank[j]}")
                if val > max_val:
                    max_val = val
        
        joltages.append(max_val)
    
    return sum(joltages) 

if __name__ == "__main__":
    answer = main()
    print(answer)
