import os
import sys
from pathlib import Path


def pause():
    input("\nНажмите Enter для продолжения...")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    files = [f for f in Path(".").rglob("*") if f.is_file() and f.suffix.lower() in {".bat", ".reg"}]

    if not files:
        print("Ошибка! Твики не найдены!")
        pause()
        sys.exit()

    while True:
        clear_screen()
        print("=== Regulus Tweaker ===")

        for i, c in enumerate(files, start=1):
            print(f"{i}. {c.name}")
        print("=======================")
        print("Введите 'q' для выхода\n")

        user_input = input("Введи номер твика для применения >> ").strip()

        if user_input.lower() == "q":
            break

        try:
            choice = int(user_input)

            if 1 <= choice <= len(files):
                selected = files[choice - 1]
                os.startfile(selected)
                pause()
            else:
                print(f"Ошибка: Введи число от 1 до {len(files)}.")
                pause()

        except ValueError:
            print("Ошибка: Введите корректное число или 'q'.")
            pause()
        except Exception as err:
            print(f"Произошла ошибка: {err}")
            pause()


if __name__ == "__main__":
    main()