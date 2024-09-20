import os
import colorama
import time

# main config

pname = "no"
repo = "Pipo-Repository-1-Win-"
repo_dilivery = "PipoPackets"
repo_url = f"https://github.com/{repo_dilivery}/{repo}.git"

def pilog(text):
    print(colorama.Fore.CYAN + "[Pipo]" + colorama.Style.RESET_ALL + " " + text)
def menu():
    os.system("cls")

    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "WARNING! Neead a git: https://git-scm.com/downloads")
    print(colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "Pipo 0.1")
    print(colorama.Style.RESET_ALL)

    pname = input("/:")

    if pname == "":
        pilog(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}No input!{colorama.Style.RESET_ALL}")
        time.sleep(3)
        menu()

    pilog(f"Create a dir for repo")
    os.system("mkdir installed")
    os.system(f"mkdir installed\{repo}")

    pilog(f"cloning a repo - {repo} by {repo_dilivery}...")

    os.system(f"git clone {repo_url} --branch {pname}")

    pilog(f"Del a repo temps and move")

    os.system(f"rmdir Pipo-Repository-1-Win-\.git /Q /S")
    time.sleep(0.4)
    os.system(f'ren Pipo-Repository-1-Win- {pname}')
    os.system(f'move {pname} installed\{repo}')
    
    pilog(f'Cheking pipo cfg...')
    
    time.sleep(0.4)

    with open(f'installed\{repo}\{pname}\pipo.cfg', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('file='):
                FILE_NAME = line.strip().split('=')[1]

    pilog(f'Launch a file: {FILE_NAME}')

    os.system("cls")

    os.system(f".\installed\{repo}\{pname}\{FILE_NAME}")

    time.sleep(2)
    menu()


menu()