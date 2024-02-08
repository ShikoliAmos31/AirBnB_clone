# x00. AirBnB clone - The console

## 0x00. Table of Contents
* [Introduction](#0x01-introduction)
* [Environment](#0x02-environment)
* [Installation](#0x03-installation)
* [Testing](#0x04-testing)
* [Usage](#0x05-usage)
* [Authors](#0x06-authors)

## 0x01. Introduction
This is a team project to build a clone of AirBnB. The console serves as a command interpreter to manage objects and their storage.

## 0x02. Environment
The project is developed and tested on:
* Operating System: Ubuntu 20.04 LTS
* Python Version: 3.8.3
* Editors: VIM 8.1.2269, VSCode 1.6.1, Atom 1.58.0
* Version Control: Git 2.25.1
* Style Guidelines: PEP8, pycodestyle (version 2.7.*)

## 0x03. Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Locozyoungg/AirBnB_clone.git
    ```
2. Navigate to the AirBnb directory:
    ```bash
    cd AirBnB_clone
    ```
3. Run the console:
    ```bash
    ./console.py
    ```

## 0x04. Testing
All tests are defined in the `tests` folder. Python unit tests are organized in the following manner:
* Modules: `python3 -c 'print(__import__("my_module").__doc__)'`
* Classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
* Functions (inside and outside a class): `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

To run the tests in interactive mode:
```bash
echo "python3 -m unittest discover tests" | bash

To run the tests in non-interactive mode:

python3 -m unittest discover tests

## 0x05. Usage
Start the console in interactive mode:

./console.py

To see available commands, use the help command:

(hbnb) help

Commands are executed in the following format:

create: Creates a new instance of a given class.
show: Retrieves an instance based on class name and ID.
destroy: Deletes an instance of a given class with a given ID.
all: Prints all string representations of all instances of a given class.
count: Prints the number of instances of a given class.
update: Updates an instance based on class name, ID, and attribute value.

## 0x06. Authors
Collins Oloo
Amos Shikoli

