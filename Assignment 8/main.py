"""
Note-taking program
"""
import os

def A(filename):
    fl = open(fileName,"r")
    print(fl.read())
    fl.close()
    exit(0)
def B(filename):
    os.remove(fileName)
    fl = open(fileName,"w")
    fl.close()
    exit(0)
def C(filename):
    textToAppend = input("Please enter the text to append:\n")
    fl = open(fileName,"a")
    fl.write(textToAppend + "\n")
    fl.close()
    exit(0)
def D(filename):
    lineNumber = int(input("Please enter line number: "))
    updatedText = input("Please provide text to update:\n")
    flag = False
    fl = open(fileName,"r")
    eachLines = [line for line in fl.readlines()]
    fl.close()
    if(lineNumber <= len(eachLines)):
        for i in range(len(eachLines)):
            if(i == (lineNumber - 1)):
                eachLines[i] = updatedText + "\n"
                flag = True
                break
        if(flag):
            fl = open(fileName,"w")
            for line in eachLines:
                fl.write(line)
            fl.close()
            exit(0)
    else:
        print("Line number is not valid. Please provide correct line number and try again.")

def Default(dummy):
    print("Please provide correct choice\n")


def switch(case):
    return{
        "A":A,
        "B":B,
        "C":C,
        "D":D
    }.get(case,Default)

fileName = input("Please enter filename: ")
isExists = os.path.isfile(fileName)
if(isExists == True):
    while(True):
        choice = input("Please select your choice(A,B,C or D) from below list\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\nYour choice is: ")
        switch(choice)(fileName)
else:
    textToWrite = input("Kindly provide text to write in file:\n")
    fl = open(fileName,"w")
    fl.write(textToWrite + "\n")
    fl.close()

