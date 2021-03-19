ofile=None
try:
    ofile=open('File Assignment/story.txt',mode='r')
    
except FileNotFoundError:
    print("File not found!!")
else:
    def AM_count():
        Acnt,Mcnt=0,0
        file_data=ofile.read()
        for ch in file_data:
            if ch[0]=='A' or ch[0]=='a':
                Acnt=Acnt+1
            elif ch[0]=='M' or ch[0]=='m':
                Mcnt+=1
        print("A or a : ",Acnt)
        print("M or m: ",Mcnt)
    AM_count()
finally:
    ofile.close()