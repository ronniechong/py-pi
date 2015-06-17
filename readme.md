#Python Pi#
A simple python app to generate Pi (using Sympy) with a defined number of decimals. It can be displayed on screen or saved as a text or json file.

##Instructions##

###Prerequisites###

Install Sympy using pip
```
sudo pip install sympy
```

or install manually (Refer to [Sympy website](http://www.sympy.org/))

###Running pi.py###

Display on screen
```
python pi.py 10
```

Saves to a text file
```
python pi.py 10 --file path/to/file.txt
```

##Parameters##
| Arguments     | Description   |
| :------------- |:------------- |
|`-h or --h`      | Help          |
|`-file or --file`| Saves to a file|
|`-json or -json` | Saves as a JSON format|

