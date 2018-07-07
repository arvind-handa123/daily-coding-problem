'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
'''

def solution(string, k):
    '''
    Keep a window and add elements to the window till it contains less or equal
    k. If unique elements exceeds than required in window, start removing the 
    elements from left side.

    Args:
        string(string)
        k(int)
    Returns:
        int: count of the length of the longest substring
    '''
    table = dict()
    slow = -1
    fast = -1
    distinct_cnt = 0
    for idx, char in enumerate(string): # iter over every char
        if char in table:   # hit in the table
            table[char] += 1
            fast = idx
        else:   # miss, means this is a new distinct char
            if len(table) == k: # the table is full, have to move from left
                while len(table) != k - 1:
                    slow += 1
                    char_slow = string[slow]
                    table[char_slow] -= 1
                    if table[char_slow] == 0:
                        table.pop(char_slow)
                table[char] = 1
                fast = idx
            else:   # table is not full, directly add it in
                table[char] = 1
                fast = idx
        if fast - slow > distinct_cnt:
            distinct_cnt = fast - slow
    return distinct_cnt

def main():
    s = 'aabbcc'
    k = 3
    print solution(s, k)

if __name__ == '__main__':
    main()
