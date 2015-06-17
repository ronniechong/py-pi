from sympy import *
import argparse

def main():
    isJSON = false
    parser = argparse.ArgumentParser(description='Outputs Pi with decimals on screen or saved as text/json file')
    parser.add_argument('length', metavar='length', type=int,help='Total decimals (excluding the leading 3.xxx)')
    parser.add_argument('--file', '-file', default = False, metavar='path/to/file.txt', type=str, help='saves results into a text file')
    parser.add_argument('--json', '-json', action='store_true', help='saves as json format')
    args = parser.parse_args()
    
    #Checks for json format
    if args.json: isJSON = True
    
    if args.file == False:
        #Output pi on screem
        print pi.evalf(args.length + 1)
    else:
        #Saves to a file
        saveFile(args.file, args.length + 1, isJSON)

def saveFile(filename, length, json):
    print 'Writing pi to ' + filename
    pre = '{pi:'
    post = '}'
    f = open(filename,'w')
    if json:
        f.write(pre + str(pi.evalf(length)) + post)
    else:
        f.write(str(pi.evalf(length)))

    f.close()

if __name__ == "__main__":
    main()
