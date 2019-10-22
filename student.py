import os

stud_data = {}

def design():
    f = open("data.txt","w")

    f.write("=====================================================\n")
    f.write(" "+format("Roll","10")+format("Name","20")+format("Phone","15")+\
            format("Marks","4")+"\n")
    f.write("=====================================================\n")

    f.close()



def load_data():
    f = open("data.txt")
    f.readline()
    f.readline()
    f.readline()

    data = f.readline().rstrip("\n")
    while data!="":
        data = data.split()
        stud_data[data[0]] = data[1:]
        data = f.readline().rstrip("\n")

    f.close()

def add_student():
    f = open("data.txt","a")
    roll = input("Enter Roll ")
    if roll in stud_data.keys():
        print ("Roll Number Already Exists Please Retry!!!!")
        return
    name = input("Enter Name ")
    phone = input("Enter Phone ")
    marks = input("Enter Marks ")

    data = " "+format(roll,"10")+format(name,"20")+format(phone,"15")+\
            format(marks,"4")+"\n"
    f.write(data)
    f.close()
    stud_data[roll]=[name,phone,marks]
    print ("Student added Successfully")

def display_all():
    print("=====================================================")
    print(" "+format("Roll","10")+format("Name","20")+format("Phone","15")+\
            format("Marks","4"))
    print("=====================================================")
    for roll in stud_data.keys():
        print(" "+format(roll,"10")+format(' '.join(stud_data[roll][:-2]),"20")+format(stud_data[roll][-2],"15")+\
            format(stud_data[roll][-1],"4"))

def display_stud():
    roll = input("Enter Student Roll")
    if roll in stud_data.keys():
        print ("Roll ",roll)
        print ("Name ",' '.join(stud_data[roll][:-2]))
        print ("Phone ",stud_data[roll][-2])
        print ("Marks ",stud_data[roll][-1])
    else:
        print ("No record Found")


def update_data():
    roll = input("Enter Roll For Upgradation")
    if roll in stud_data.keys():
        f = open("temp.txt","w")
        f2 = open("data.txt","r")
        f.write(f2.readline())
        f.write(f2.readline())
        f.write(f2.readline())
        new = [roll]
        s = f2.readline()
        while s!='':
            if roll != s.split()[0]:
                f.write(s)
            else:
                s = s.split()
                print ("Name ",' '.join(s[1:-2]))
                ch = input("Do you want to update(Y/n)")
                if ch=='y' or ch =='Y':
                    name = input("Enter Updated Name ")
                    new.append(name)
                else:
                    new.append(' '.join(s[1:-2]))

                print ("Phone ",s[-2])
                ch = input("Do you want to update(Y/n)")
                if ch=='y' or ch =='Y':
                    phn = input("Enter Updated Phone ")
                    new.append(phn)
                else:
                    new.append(s[-2])

                print ("Marks ",s[-1])
                ch = input("Do you want to update(Y/n)")
                if ch=='y' or ch =='Y':
                    mrk = input("Enter Updated MArks ")
                    new.append(mrk)
                else:
                    new.append(s[-1])

                f.write(" "+format(new[0],"10")+format(new[1],"20")+format(new[2],"15")+format(new[3],"4")+"\n")
                stud_data[roll] = new[1:]
            s = f2.readline()
        f.close()
        f2.close()
        os.replace("temp.txt","data.txt")
                    
    else:
        print ("No Record Found")


def main():
    if not os.path.exists("data.txt"):
        design()
    load_data()
    while True:
        print ("Enter Your Choice(1-8)")
        print ("1. Add Student")
        print ("2. Display All Students")
        print ("3. Display Student Data with Roll")
        print ("4. Update Student record")
        print ("To Exit Press -1 ")
        ch = int(input())
        if ch == 1:
            add_student()
        elif ch == 2:
            display_all()
        elif ch == 3:
            display_stud()
        elif ch == 4:
            update_data()
        elif ch == -1:
            break
main()

    
