import re
def count_substring(string,substring):
    cnt = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            cnt += 1
    return cnt
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
