import os
from pathlib import Path
import subprocess

files = [f for f in Path(".").rglob("*") if f.is_file() and f.suffix.lower() in {".bat", ".reg"}]


print(files)

def pause():
    print("Нажмите Enter для продолжения...")
    input()

while True:
    print("Regulus Optimizer")
    for i, c in enumerate(files, start=1):
        print(f"{i}. {c.name}")
    try:
        file_num = int(input("Введи номер твика для применения >> "))
        if 1 <= file_num <= len(files):
            selected = files[file_num - 1]
            os.startfile(selected)
            pause()
        else:
            print("Try Again")
            pause()
        
        
    except Exception as err:
        print(err)
        pause()

    

