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

    similarity_score = 0
    for number in first_colum:
        similarity_score += number * second_column.count(number)
    print(similarity_score)

if __name__ == '__main__':
    main()