
def main():
    # inputfile  = "test_input.txt"
    inputfile  = "input.txt"

    with open(inputfile, 'r') as fd:
        first_colum = []
        second_column = []
        for line in fd.readlines():
            split_array = line.split()
            first_colum.append(int(split_array[0]))
            second_column.append(int(split_array[1]))
    
    first_colum.sort()
    second_column.sort()
    
    total_sum = 0
    for col1, col2 in zip(first_colum, second_column):
        total_sum += abs(col2 - col1)

    print(total_sum)

if __name__ == '__main__':
    main()