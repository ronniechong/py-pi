# Python Pi
A simple python script to generate Pi with a defined number of decimals (excluding the leading 3.xxxx). It can be displayed on screen or saved as a text or json file.

## Instructions

### Prerequisites
The script requires Sympy to calculate the Pi

Install Sympy using pip
```
pip install sympy
```

or install manually (refer to [Sympy website](http://www.sympy.org/))

### Running pi.py

Display on screen
```
python pi.py 10
>> 3.1415926536
```

Saves to a text file
```
python pi.py 10 --file path/to/file.txt
```

## Parameters
| Arguments     | Description   |
| :------------- |:------------- |
|`-h or --help`      | Help          |
|`-f or --file`| Saves to a file|
|`-j or --json` | Saves as a JSON format|
|`-v or --verbose` | Verbose mode|

