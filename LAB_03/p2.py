# Q.2. Given a string s, find the length of the longest substring without repeating characters in O(n) time

# Examples:

# Input: "ABCBC Output: 3 
# Explanation. The longest substring without repeating characters is 
# "ABC" 
# Input: "AAA" Output: 1 Explanation. The longest substring without repeating characters is "A"
string = str(input("entrer the string:- "))
start = 0
end = 0
lis = [0]*26
max_len = 0
while(end<len(string)):
    idx = ord(string[end]) - ord('a')
    while(lis[idx]>0):
        lis[ord(string[start]) - ord('a')] = 0
        start +=1
    lis[idx] = 1
    max_len = max(max_len,end-start+1)
    end +=1
print(max_len)

