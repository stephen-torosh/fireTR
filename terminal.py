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


def listCommands():
    print(f"{bcolors.OKGREEN}Available commands:{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}ls - show all files in current directory{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}mkdir - create directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}rmdir - remove directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}cat - read file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}crf - create file in directory name{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}version - current version of fireTR{bcolors.ENDC}")


def command(value):
    match value:
        case "ls":
            directory = input("-> Enter directory path: ")
            ls(directory)
        case "mkdir":
            directoryName = input("-> Enter directory name: ")
            mkdir(directoryName)
        case "rmdir":
            directoryName = input("-> Enter directory name: ")
            rmdir(directoryName)
        case "crf":
            filePath = input("-> Enter file path: ")
            createFile(filePath, "Hey guys")
        case "cat":
            fileName = input("-> Enter file name: ")
            cat(fileName)
        case "version":
            print("version: 0.4")
        case "help":
            listCommands()
        case "clear":
            clearScreen()
        case _:
            listCommands()


# Application start

# Initialize colorama
init()

version = "0.4"
print(
    f"-> Welcome to {Fore.GREEN}{Style.DIM}fireTR {version}{Style.RESET_ALL}\n")

while True:
    commandEnterred = input("-> ")
    command(commandEnterred)
