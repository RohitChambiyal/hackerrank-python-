def split_and_join(line):
    line = line.split(" ")
    # takes seperation using " " and makes a list
    line = "-".join(line)
    # joins using "-" all seperated list items
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
