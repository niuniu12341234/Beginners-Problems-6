print ("===Is it a Triangle?===")
def triangle(side1, side2, side3):
    if (side1+side2 <= side3 or side1+side3 <= side2 or side2+side3 <= side1):
        print ("It cannot be a triangle.")
    else:
        print ("It is a triangle.")
triangle(33,4,30)
print ("===Greetings!===")
name = input ("What is your name?\n>>")
time = int(input("What time is it?\n>>"))
def greetings(time,name):
    if (12>=time>=0):
        print ("Good morning,",name,"!")
    if (17>=time>=13):
        print ("Good afternoon,",name,"!")
    if (24>=time>=18):
        print ("Good evening,",name,"!")
greetings(time,name)
print("===Even Numbers===")
num = [4,34,25,36,7,8,9,0]
even =[]
def getEven():
    return [i for i in num if i%2 == 0]
print (getEven())
