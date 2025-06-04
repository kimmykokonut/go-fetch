# Go Fetch!
_by [Kim Robinson](https://github.com/kimmykokonut/)_

A take-home coding exercise

## 🎯 Requirements: Storing and Fetching Values
- Your challenge will be to create a command line tool for storing and fetching key-value pairs. In other words, given a key and a value, which are both strings, it can store key and value together, and then return that value when fetched by that key. Running the tool must open an interactive session that accepts put, fetch, and exit commands. When ready to accept a command, it must output the string "> " as a command prompt.

- The put command should accept a key and a value, for example, "put favorite_color
purple". That value should then be stored with that key. If the key already exists in the system, the old value should be discarded. If successful, the command should output the string "ok".

- The fetch command should just accept a key, for example, fetch favorite_color. If a
value with that key has been entered, it should output that value ("purple"). If no value has been entered for that key, it should output the string "Value not found."

- The exit command should output the string "Bye!" and exit the program.

- If any other command is entered, it should output the string "Unknown command. Known
commands are: put, fetch, exit".

- If a command has the wrong number of arguments or is otherwise malformed, it should output the string "Invalid syntax."

- Example session:
Here is an example of what a full session might look like. The first line represents running the program from your terminal. This is just example input -- your program should accept any reasonable strings as names and values.
```
$ ./key-value
> put favorite_color purple
ok
> put favorite_flavor strawberry
ok
> fetch favorite_color
purple
> fetch favorite_animal
value not found
> exit
Bye!
```

## ⌛ Setup

### Clone repository

1. Navigate to the [repository](https://github.com/kimmykokonut/go-fetch).
2. Click the `Fork` button and you will be taken to a new page where you can give your repository a new name and description. Choose "create fork".
3. Click the `Code` button and copy the url for HTTPS.
4. On your local computer, create a working directory of your choice.
5. In this new directory, via the terminal, type `$ git clone https://github.com/kimmykokonut/go-fetch`.
6. View or Edit: On your terminal, navigate to `src/go_fetch`, type `$ code .` to open the project in VS Code.

### Install dependencies and run local server
1. If you do not have Python on your local environment, I recommend installing via Homebrew.  Otherwise you can download Python [here](https://www.python.org/downloads/)
  - Install [Homebrew](https://brew.sh/)
  - Install Python `$ brew install python`
  - Verify installed and version number: `$ python3 --version`
2. Run go fetch script: `$ python3 main.py`

## 🔧 Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
