import pickle

def add_emp_record():
    file = open("employee.dat","ab")
    emp = {}        #Dictionary with name emp is created
    #Reading input from user to enter into dict
    emp['empcode'] = int(input("Enter employee code: "))
    emp['name'] = input("Enter employee Name: ")
    emp['salary'] = int(input("Enter salary: "))
    pickle.dump(emp, file)
    file.close()
    
def searchEmp():
    file = open("employee.dat","rb")
    try:
        while True:
            emp = pickle.load(file)
            #employee salary > 30000
            if emp['salary']>30000:
                print(emp)
    except EOFError:
        print("\nFile Ended")
    file.close()


while True:
    add_emp_record()
    choice = input("Wanna add more employees (y/n)? ")
    if choice=='N' or choice=='n':
        print("\n\nStopped adding employess")
        break

print('\n\nEmployees who are having salary more than 30000')
searchEmp()
