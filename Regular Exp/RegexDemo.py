import re

#Simple example to xtract name and ages from string
str='''
Hemlata is 21 and Akash is 18
Nikhil is 23
'''

print("splitted string:",str.split())
print("line splited string: ", str.splitlines())    #split new lines
ages=re.findall(r'\d{1,3}',str)
names=re.findall(r'[A-Z][a-z]*',str)

namaAgeDict={}

x=0
for nm in names:
    namaAgeDict[nm]=ages[x]
    x=x+1

print(namaAgeDict)

#search() over findall()
str="I was searching for peace, and I'm feeling so peaceful here"
if(re.search("peace",str)):
    print("desired string found")

res=re.findall("peace",str)
print(res)
str="hemlata Ahire"
print("Mathcing",re.match("ahire",str))
# simple program to validate emial addess
emails="'hemlata@gmail.com','akshaya.ahire23@xyz','@Sam.com','honk.com@gmail.com'"
cemails=re.findall("[\w./*&%]{2,20}@[\w./*&%]{1,10}.[A-Za-z]{2,5}",emails)
print("valid emails are using findAll : ",cemails)
cemails=re.search("[\w./*&%]{2,20}@[\w./*&%]{1,10}.[A-Za-z]{2,5}",emails)
print("valid emails are using search : ",cemails)       #Only first matching output will be printed
cemails=re.match("[\w./*&%]{2,20}@[\w./*&%]{1,10}.[A-Za-z]{2,5}",emails)
print("valid emails are using match : ",cemails)



#Sample web Scrapping
"""
import urllib.request
import re

url= "https://www.summet.com/dmsi/html/codesamples/addresses.html"
response=urllib.request.urlopen(url)
respHtml=response.read()
htmlStr=respHtml.decode()
data=re.findall("\(\d{3}\) \d{3}-\d{4}",htmlStr)
print(data)
"""