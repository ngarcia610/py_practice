# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

def change(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)

def swap_case(s):
    return ''.join(map(change, s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)