import csv

def setup_csv():
    puzzle = ""
    with open('./puzzle.txt', 'r') as file:
        for line in file:
            puzzle += line
            
    puzzle_lines = [x.split(" ") for x in puzzle.split("\n")]

    with open('puzzle.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in puzzle_lines:
            csvwriter.writerow(line)
            
def check_row(row):
    num_row = [int(x) for x in row]
    sorted_row = sorted(num_row)
    
    if num_row != sorted_row and num_row != sorted_row[::-1]:
        return False
        
    for i in range(0, len(num_row)-1):
        if num_row == sorted_row:
            if not (((num_row[i+1] - num_row[i]) < 4) and ((num_row[i+1] - num_row[i]) > 0)):
                return False
        else:
            if not (((num_row[i] - num_row[i+1]) < 4) and ((num_row[i] - num_row[i+1]) > 0)):
                return False
            
    return True
        
            
def solve():
    setup_csv()
    
    data = []
    with open('puzzle.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([int(value) for value in row])
    
    safe_reports = 0
    for row in data:
        if check_row(row):
            safe_reports += 1
            
    print(safe_reports)
    
if __name__ == "__main__":
    solve()