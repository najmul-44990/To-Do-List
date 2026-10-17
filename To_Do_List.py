#To-Do List	List, Loops, Functions
list=["HTML","Python","C","C++","Jhava"]
def vew_task():
    f=len(list)
    print(list[0:f])

def add_task():
    n=input("Enter the new work: ")
    a=0
    for i in range (0,len(list)):
        if(n!=list[i]):
            a=0
        else:
            a=1
            break
    if(a==0):
        list.append(n)

def Delat_task():
    m=input("Enter delate work: ")
    b=-1
    for i in range(0,len(list)):
       if(m==list[i]):
         b=i
         break
    if(b!=-1):
        list.pop(b)
    else:
        print("Task not found!")
    


while(True):
    print("Enter 1 add task, enter 2 vew task,enter 3 delate task enter 0 off the work: ")
    p=int(input())
    if(p==1):
        add_task()
    elif(p==2):
        vew_task()
    elif(p==3):
        Delat_task()
    elif(p==0):
        print("Thank you!")
        break