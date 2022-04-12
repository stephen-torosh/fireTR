import os
from os import system
from colorama import init, Fore, Style
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


    

def ls(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        for f in files:
            print(f)
    else:
        print(f"{bcolors.FAIL}-> FTR: directory not found{bcolors.ENDC}")


def mkdir(path):
    try:
        os.mkdir(path)
        print(
            f"{bcolors.OKGREEN}-> FTR: Directory '{path}' successfully created{bcolors.ENDC}")
    except FileExistsError as error:
        print(f"{bcolors.FAIL}-> FTR: failed to create directory{bcolors.ENDC}")


def rmf(filePath):
    try:
        os.remove(filePath)
        print(
            f"{bcolors.OKGREEN}-> FTR: File '{filePath}' successfully removed{bcolors.ENDC}")
    except FileExistsError as error:
        print(f"{bcolors.FAIL}-> FTR: file not found{bcolors.ENDC}")


def cd(path):
    try:
        os.chdir(path)
        print(
            f"{bcolors.OKGREEN}-> FTR: Current directory successfully defined{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}-> FTR: Current directory does not exists{bcolors.ENDC}")


def rmdir(path):
    if os.path.isdir(path):
        os.rmdir(path)
        print(
            f"{bcolors.OKGREEN}-> FTR: Directory '{path}' successfully removed{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}-> FTR: direcotry not found{bcolors.ENDC}")


def cat(path):
    if os.path.isfile(path):
        with open(path) as f:
            contents = f.read()
            print(contents)
    else:
        print(f"{bcolors.FAIL}-> FTR: file not found{bcolors.ENDC}")


def createFile(filePath, textLine):
    with open(filePath, 'w') as f:
        f.write(textLine)
    print(f"{bcolors.OKGREEN}-> FTR: File '{filePath}' successfully created{bcolors.ENDC}")


def clearScreen():
    system('cls')


def listCommands():
    print(f"{bcolors.OKGREEN}Available commands:{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}ls - show all files in current directory{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}mkdir - create directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmdir - remove directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cat - read file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}crf - create file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}version - current version of fireTR{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmf - remove file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cd - set the desired current directory to work with it{bcolors.ENDC}")


def command(value):
    match value:
        case "ls":
            ls(interpretatedCommandEnterred[1])
        case "cd":
            cd(interpretatedCommandEnterred[1])
        case "mkdir":
            mkdir(interpretatedCommandEnterred[1])
        case "rmdir":
            rmdir(interpretatedCommandEnterred[1])
        case "crf":
            txtInFile = input("-> FTR: Enter Text to this file: ")
            createFile(interpretatedCommandEnterred[1], txtInFile)
        case "rmf":
            rmf(interpretatedCommandEnterred[1])
        case "cat":
            cat(interpretatedCommandEnterred[1])
        case "version":
            print("FTR: version: 1.1 official")
        case "help":
            listCommands()
        case "restart":
            time.sleep(1)
            os.chdir(".")
            start()
        

            
            
            
       

# Application start


# Initialize colorama
init()

def start():
    os.chdir(".")
    print("FireTR 1.1 official\n")
    print("Copyright (c) FireInc corporation\n")
    print("Type 'help' to get help\n")

start()

while True:
    commandEnterred = input("FTR " + os.getcwd() + " #: ")
    interpretatedCommandEnterred: list = commandEnterred.split()
    try:
        command(interpretatedCommandEnterred[0])
    except:
        pass
