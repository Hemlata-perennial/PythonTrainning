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
    print(c,(slen +1)/2)
    if c > (slen +1)/2: 
        pass
    A.extend(c * x)
    print(A)
res = [None] * slen 

#split
res[::2] = A[int(slen /2):]     #to fillreapeated characters by skip of 2 and strt with 0
res[1::2]= A[:int(slen /2)]     #to fill empty spaces with non-reapeaed character
#Join
print("Possible arranged string is")
print("".join(res))
