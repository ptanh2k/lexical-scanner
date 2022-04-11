# Lexical Scanner for Compiler class

---

### Technology used

- Language: Python (ver 3.9.2)
- Editor: VS Code
- OS: Windows 10

### Project structure

This project contains these following files:

- Automaton.py
- Error.py
- Output.py
- Symbols.py
- LexicalScanner.py
- main.py

All files should be in the same directory. In my case, I used the root directory

### How to run

Run the following command in terminal:

```
python main.py -i <Path to source code file>
```

In case you have multiple python version installed on your machine (ex: python 2.x and python 3.x), you can run:

```
python3 main.py -i <Path to source code file>
```

Example:

```
python main.py -i input.vc
```

Since this project was developed for VC code file, your source code file extension should be .vc
