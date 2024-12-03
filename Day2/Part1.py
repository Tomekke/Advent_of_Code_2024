def main():
    # inputfile  = "test_input.txt"
    inputfile  = "input.txt"

    safe = unsafe = number_of_lines = steps = 0
    with open(inputfile, 'r') as fd:
        for report in fd.readlines():
            # print(report)
            report = report.strip().split()
            report = [ int(x) for x in report ]
            sorted_report, reverse_sorted_report = [], []
            sorted_report.extend(report)
            reverse_sorted_report.extend(report)
            sorted_report.sort()
            reverse_sorted_report.sort(reverse=True)

            for level in range(1, len(report)):
                # Going Up
                if report == sorted_report:
                    steps = report[level] - report[level - 1]
                # Going Down
                elif report == reverse_sorted_report:
                    steps = report[level - 1] - report[level]
                else:
                    unsafe += 1
                    break
                if steps < 1 or steps > 3:
                    unsafe += 1
                    break
            number_of_lines += 1
    safe = number_of_lines - unsafe
    print(safe, unsafe)

if __name__ == '__main__':
    main()