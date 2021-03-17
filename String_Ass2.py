print("Enter String to start ")
"""
Problem Statement: 

Kevin and Stuart want to play the 'The Minion Game'.
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
 
I.e BANANA
 
If the string is BANANA, the substrings are:
B
BA
BAN
BANA
BANAN
BANANA
A
AN
ANA
ANAN
ANANA
N
NA
NAN
NANA
A
AN
ANA
N
NA
A
 """


Str = input()
S_len = len(Str)
p1_Name="Kevin"
p2_Name="stuard"

print(p1_Name," will create string with vowel")
print(p2_Name," will create string with Constants")
for j in range(S_len):           #iterate through string
    nstr=Str[j:S_len]
    print("new string to play: ",nstr)
    nstr_len=len(nstr)
    for i in range(nstr_len): 
        if nstr[i] in "AEIOU":             #check for vowels
            #print("\nVowels found!! it's ",p1_Name,"'s turn to play")
            #print(p1_Name,"Created substring :")    #create strings with vowels
            print(nstr[:i+1])
        else:
            #print("\nConstant found!! it's ",p2_Name,"'s turn to play")
            #print(p2_Name,"Created substring :")    #create string with constants
            print(nstr[:i+1])      