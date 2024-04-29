import os
import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_contents(path, prefix=''):
    if not os.path.exists(path):
        print(Fore.RED + f"Помилка: Шлях {path} не існує." + Style.RESET_ALL)
        return
    
    if not os.path.isdir(path):
        print(Fore.RED + f"Помилка: Шлях {path} не є директорією." + Style.RESET_ALL)
        return
    
    try:
        for entry in sorted(os.listdir(path)):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(Fore.BLUE + prefix + "📂 " + entry + Style.RESET_ALL)
                print_directory_contents(full_path, prefix + "  ")
            else:
                print(Fore.GREEN + prefix + "📜 " + entry + Style.RESET_ALL)
    except PermissionError:
        print(Fore.RED + f"Помилка: Немає дозволу доступу до {path}." + Style.RESET_ALL)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Використання: python hw03.py [шлях до директорії]")
    else:
        print_directory_contents(sys.argv[1])
