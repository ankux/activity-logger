print("Health Management System")

def getdate():
    import datetime
    return datetime.datetime.now()

name = ['Harry', 'Rohan', 'Hammad']

inp = int(input("\tHello, Welcome!\nFor Log: Type 1 \nFor retrieve: Type 2\n"))

def name1():
    inp_name = int(input("Which client do you want to see:\n1: Harry\n2: Rohan\n3: Hammad\n"))
    return inp_name

if inp == 1:
    n = name1()
    inp_log1 = input("What you want to log:\n1: Food\n2: Exercise\n")
    if inp_log1 == 1:
        file = name[n-1] + "food.txt"
        data1= input("Now you can log\n")
        data1.write(str(getdate())+"\t\t" + data)
        data1.close()
    else:
        file = name[n-1]+"exercise.txt"
        data1=open(file,"a")
        data=input("Now you can log\n")
        data1.write(str(getdate())+"\t\t" + data)
        data1.close()
if inp == 2: 
    