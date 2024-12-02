import csv
import pandas as pd

def setup_csv():
    puzzle = ""
    with open('./puzzle.txt', 'r') as file:
        for line in file:
            puzzle += line
            
    puzzle_lines = [x.split("   ") for x in puzzle.split("\n")]

    with open('puzzle.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in puzzle_lines:
            csvwriter.writerow(line)
    
    df = pd.read_csv('puzzle.csv', header=None)
    sorted_df = df.apply(lambda x: sorted(x), axis=0)
    
    sorted_df.to_csv('sorted_puzzle.csv', header=False, index=False)


def solve():
    setup_csv()
    
    data = []
    with open('sorted_puzzle.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([int(value) for value in row])
    
    total_diff = 0
    for row in data:
        total_diff += abs(row[1] - row[0])

    print(total_diff)
        
if __name__ == "__main__":
    solve()