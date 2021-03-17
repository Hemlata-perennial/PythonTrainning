"""
that no two adjacent characters are same.

Input: aaabc 
Output: abaca 

Input: aaabb
Output: ababa
 """
print("Enter any string: ")

S=input()
slen = len(S)
A = []
#Sort string
for c, x in sorted((S.count(x), x) for x in set(S)):
    if c > (slen +1)/2: print("")
    A.extend(c * x)
    print(A)
res = [None] * slen 
print(res)
#split
res[::2],res[1::2] = A[int(slen /2):], A[:int(slen /2)]

#Join
print("Possible arranged string is")
print("".join(res))
