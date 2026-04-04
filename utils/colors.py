from colorama import Fore

def header(text):
    print(Fore.CYAN + text)

def info(text):
    print(Fore.GREEN + text)

def warning(text):
    print(Fore.RED + text)

def menu_option(text):
    print(Fore.YELLOW + text)

def menu_header(text):
    print(Fore.MAGENTA + text)