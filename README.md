# Regulus 

Regulus — консольный твикер и менеджер скриптов для Windows, предназначенный для удобного поиска и запуска системных настроек и оптимизаций через файлы `.bat` и `.reg`.

> **Обратите внимание:** В программе **нет встроенных твиков**. Regulus работает как загрузчик/оболочка: вы сами добавляете нужные вам скрипты и твики реестра в директорию программы.

## Возможности

- **Без лишнего балласта:** программа не навязывает сторонние твики — вы используете только проверенные лично вами скрипты.
- Автоматический поиск файлов `.bat` и `.reg` в текущей директории и всех вложенных папках.
- Поддержка пакетных файлов Windows (`.bat`) и файлов реестра (`.reg`).
- Удобный выбор нужного твика по номеру в консоли.
- Запуск выбранного файла непосредственно из меню программы.

## Как добавить твики

1. Поместите ваши файлы `.bat` и `.reg` в папку с программой (можно организовывать их по вложенным папкам, например `tweaks/network`, `tweaks/ui` и т. д.).
2. Запустите утилиту — она автоматически просканирует директорию и выведет все найденные скрипты единым списком.

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите программу:
   ```bash
   python main.py
   ```

Regulus просканирует папки и отобразит пронумерованный список доступных файлов. Введите номер нужного твика и нажмите **Enter**, чтобы запустить его.

## Требования

- Windows 10 или Windows 11
- Python 3.8 или новее
- Библиотека `colorama` (`pip install -r requirements.txt`)

## Важная информация

Regulus выполняет запуск переданных вами файлов. Некоторые твики могут изменять системный реестр и критические параметры Windows. Всегда проверяйте содержимое файлов перед запуском. Используйте программу на свой страх и риск.

---

# Regulus (English)

Regulus is a command-line Windows tweaking manager designed to organize and execute system optimizations via `.bat` and `.reg` files.

> **Note:** Regulus **does not include built-in tweaks**. It acts as a runner/manager: you add your own trusted batch scripts and registry files to the folder.

## Features

- **Clean & transparent:** no pre-packaged tweaks or hidden scripts — run only what you inspect and provide yourself.
- Automatically scans the current directory and all subfolders for `.bat` and `.reg` files.
- Supports both Windows batch scripts and registry import files.
- Simple numbered list selection directly in the console.
- Launches selected tweaks on demand without leaving the tool.

## Adding Tweaks

1. Copy your `.bat` and `.reg` files into the program directory (you can organize them into subfolders such as `tweaks/system`, `tweaks/privacy`, etc.).
2. Run the application — it will discover and index all valid files automatically.

## Installation & Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the program:
   ```bash
   python main.py
   ```

Regulus will list all detected tweaks with assigned numbers. Type the number of the script you want to run and press **Enter**.

## Requirements

- Windows 10 or Windows 11
- Python 3.8 or newer
- `colorama` library (`pip install -r requirements.txt`)

## Disclaimer

Regulus runs the scripts provided by the user. Modifying system settings or registry keys carries inherent risks. Always inspect scripts before executing them. Use at your own risk.