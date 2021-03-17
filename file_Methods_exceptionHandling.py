try:
    f = open('sample1.txt',mode='w+', encoding = 'utf-8')
except:
  print("An exception occurred while opening file")

else:
    # do file operations.
    f.write('It is my first file\n')
    #second line
    f.write('This file\n')
    #third line
    f.write('contains three lines\n')

    data = f.read(19);
    print('Read String is : ', data)

        #Check current position
    position = f.tell();
    print('Current file position : ', position)

        #Reposition pointer at the beginning once again
    position = f.seek(0, 0);
    data = f.read(19);
    print('Again read String is : ', data)
finally:
   f.close()

