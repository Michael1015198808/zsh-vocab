import os
import json
from sys import argv
from sys import stderr
def read():
    try:
        with open(os.path.expanduser("~/.vocab/data.json"),"r") as f:
            try:
                words=json.load(f)
            except json.decoder.JSONDecodeError:
                print(os.path.expanduser("~/.vocab/data.json"+" can't be decoded."),file=stderr)
                print("See if it's set to a wrong authority",file=stderr)
                print("or the file is broken",file=stderr)
                words=[]
        return words
    except FileNotFoundError:
        print(os.path.expanduser("~/.vocab/data.json"+" is not found."),file=stderr)
        print("call "+argv[0]+" help for more information",file=stderr)

def write(words):
    try:
        with open(os.path.expanduser("~/.vocab/data.json"),"w") as f:
            json.dump((words),f)
    except FileNotFoundError:
        print(os.path.expanduser("~/.vocab/data.json"+" is not found."),file=stderr)
        print("call "+argv[0]+" help for more information",file=stderr)
