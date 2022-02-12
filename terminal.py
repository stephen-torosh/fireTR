import os
from os import system
from colorama import init, Fore, Style


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
        print(f"{bcolors.FAIL}-> directory not found{bcolors.ENDC}")


def mkdir(path):
    try:
        os.mkdir(path)
        print(
            f"{bcolors.OKGREEN}-> Directory '{path}' successfully created{bcolors.ENDC}")
    except FileExistsError as error:
        print(f"{bcolors.FAIL}-> filed to create directory{bcolors.ENDC}")


def rmf(filePath):
    try:
        os.remove(filePath)
        print(
            f"{bcolors.OKGREEN}-> File '{filePath}' successfully removed{bcolors.ENDC}")
    except FileExistsError as error:
        print(f"{bcolors.FAIL}-> file not found{bcolors.ENDC}")


def cd(path):
    try:
        os.chdir(path)
        print(
            f"{bcolors.OKGREEN}-> Current directory successfully defined{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}-> Current directory does not exists{bcolors.ENDC}")


def cdRestartType():
    os.chdir(".")


def rmdir(path):
    if os.path.isdir(path):
        os.rmdir(path)
        print(
            f"{bcolors.OKGREEN}-> Directory '{path}' successfully removed{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}-> direcotry not found{bcolors.ENDC}")


def cat(path):
    if os.path.isfile(path):
        with open(path) as f:
            contents = f.read()
            print(contents)
    else:
        print(f"{bcolors.FAIL}-> file not found{bcolors.ENDC}")


def createFile(filePath, textLine):
    with open(filePath, 'w') as f:
        f.write(textLine)
    print(f"{bcolors.OKGREEN}-> File '{filePath}' successfully created{bcolors.ENDC}")


def clearScreen():
    system('cls')


def restart():
    clearScreen()
    cdRestartType()
    print("FireTR 1.0 official\n")
    print("Copyright fireINC corporation\n")
    print("Launching with PowerShell or Python 3.10\n")
    print("Type 'help' to get help\n")


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
    print(f"{bcolors.OKGREEN}clear - clear all screen{bcolors.ENDC}")


def command(value):
    match value:
        case "ls":
            directory = input("-> Enter directory path: ")
            ls(directory)
        case "cd":
            directoryName = input(
                "-> enter the desired current directory to work with it: ")
            cd(directoryName)
        case "mkdir":
            directoryName = input("-> Enter directory name: ")
            mkdir(directoryName)
        case "rmdir":
            directoryName = input("-> Enter directory name: ")
            rmdir(directoryName)
        case "crf":
            filePath = input("-> Enter file path: ")
            txtInFile = input("-> Enter Text to this file: ")
            createFile(filePath, txtInFile)
        case "rmf":
            filePath = input("-> Enter file path: ")
            rmf(filePath)
        case "cat":
            fileName = input("-> Enter file name: ")
            cat(fileName)
        case "version":
            print("version: 1.0 official")
        case "help":
            listCommands()
        case "clear":
            clearScreen()
        case "restart":
            restart()
        case _:
            listCommands()

# Application start


# Initialize colorama
init()

print("FireTR 1.0 official\n")
print("Copyright fireINC corporation\n")
print("Launching with PowerShell or Python 3.10\n")
print("Type 'help' to get help\n")

while True:
    commandEnterred = input("FTR " + os.getcwd() + " #: ")
    command(commandEnterred)
