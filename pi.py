from sympy import *
import argparse, time, json

def main():
    isJSON = false
    timeStart = time.clock()
    isVerbose = false
    parser = argparse.ArgumentParser(description='Outputs Pi with defined number of decimals on screen or saves as a text or json format file')
    parser.add_argument('length', metavar='length', type=int,help='Total decimals (excluding the leading 3.xxx)')
    parser.add_argument('--file', '-f', default = False, metavar='path/to/file.txt', type=str, help='saves result to a text file')
    parser.add_argument('--json', '-j', action='store_true', help='saves as json format')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')
    args = parser.parse_args()
    
    #Checks for json format
    if args.json: isJSON = True
    if args.verbose: isVerbose = True
    
    if args.file == False:
        #Output pi on screen
        if isVerbose: print 'Output Pi with', str(args.length), 'decimals:'

        print pi.evalf(args.length + 1)

    else:
        #Saves to a file
        if isVerbose:
            if isJSON:
                print 'Saving as JSON format'
            else:
                print 'Saving as text format'

        saveFile(args.file, args.length + 1, isJSON)

    if isVerbose:  print 'Done in', time.clock() - timeStart, 'seconds'

def saveFile(filename, length, isJson):
    print 'Writing Pi to', filename

    f = open(filename,'w')
    
    if isJson:
        json.dump({'pi':str(pi.evalf(length))},f,indent=4)
    else:
        f.write(str(pi.evalf(length)))
    
    f.close()

if __name__ == "__main__":
    main()
