#!/usr/bin/python
import sys, os, getopt

def replace_in_file( files, trg, rpl ):
    change_count =0
    for file in files:
        print("Replacing {} for {} in {}".format(trg, rpl, file))
        try:
            with open(file, 'r') as fp:
                buffer = fp.read()
                fp.close()
                fp = open(file, 'w')
                fp.write(buffer.replace(trg, rpl))
                fp.close()
                change_count+=1
        except FileNotFoundError as err:
            print("File {} not found.".format(file))
        except IsADirectoryError as err:
            print("{} is a directory, ignoring...".format(file))
        except UnicodeError as err:
            print("Cannot read {} file, ignoring...".format(file))
        except Exception as err:
            print("Cannot read {} file, ignoring...".format(file))
    print("Replaced {} for {} in {} files".format(trg, rpl, change_count))

def change_file_names( files, trg, rpl ):
    for file in files:
        if file.find(trg, 0,-1) < 0:
            continue
        try:
            with open(file, 'r') as fp:
                buffer = fp.read()
                fp.close()
                os.remove(file)
                new_file = file.replace(trg, rpl)
                print("{} moved to {}".format(file, new_file))
                fp = open(new_file, 'a')
                fp.write(buffer)
                fp.close()
        except FileNotFoundError as err:
            print("File {} not found.".format(file))
        except IsADirectoryError as err:
            print("{} is a directory, ignoring...".format(file))
    print("Replaced {} for {} in {} filenames".format(trg, rpl, change_count))
        

def main():
    files = []
    file_names = False
    target = ""
    replacement = ""
    s_options = "if:t:r:"
    l_options = ["includenames","files", "target=", "replacement="]
    try:
        args, params = getopt.getopt(sys.argv[1:], s_options, l_options)
    except getopt.error as err:
        print("Invalid option")
        sys.exit(2)
    count = 0
    for arg, param in args:
        if arg in ("-f", "--files"):
            if param.find(' ')  < 0:
                files.append(param)
            else:
                files = param.split(' ')
        elif arg in ("-t", "--target"):
            target = param
        elif arg in ("-r", "--replacement"):
            replacement = param
        elif arg in ("-i", "--includenames"):
            file_names  =True
        else:
            print('Unrecognized option "{}"'.format(arg))
            sys.exit(2)
        count+=1
    if (target == "" or replacement == ""):
        print("Error: Need to set both target (-t, --target=) and replacement (-r, --replacement)")
        sys.exit(2)
    replace_in_file(files, target, replacement)
    if(file_names):
        change_file_names(files, target, replacement)

if __name__ == "__main__":
    main()
