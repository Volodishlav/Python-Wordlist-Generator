# Python Wordlist Generator

A wordlist generator written in Python.

## Features

* Handles large generation targets
* Randomized username composition
* Prefix/suffix mutation
* Hyphenated and concatenated formats
* Seeded randomness
* Exports directly to **.txt**
* Lightweight and dependency-free

## Settings

```python
# Base words:
base = [
    "admin",
    "root",
    "user"
]

# Prefixes:
prefixes = ["", "x", "y", "z", "a", 
    "b", "c", "alpha", "beta"
]

# Suffixes:
suffixes = ["", "a", "b", "c", "01",
    "02", "03", "001"
]

# Numeric Variants:
num_variants = ["1","2","3","01","02","03",
    "001","002","003","100","101","200",
    "201","301","302","400","500","123"
]

# Change target size:
TARGET = 1000000

# Change max generation attempts:
max_attempts = 2000000

# Change separators:
separators = ["", ".", "-", "_"]
```

## Requirements

- Python 3.9+

## Usage

```bash
git clone https://github.com/Volodishlav/Python-Wordlist-Generator
cd Python-Wordlist-Generator
```

```bash
python3 main.py
```

The generated wordlist will be exported to the current directory as **"wordlist.txt"**

## Example Generated Patterns

```txt
admin123
root-123
xadmin01
betauser
adminroot500
user-user-dev
rootstage123
newadmin
adminadmin_001
v2roottest
```

## Disclaimer

This tool is intended for educational purposes, research and password auditing. The author is not responsible of any misuse or damage caused by it
