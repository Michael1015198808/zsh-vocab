from include import *
from word import *
from random import randint
from random import random
def display(cmd,effe,cmdlen=15,indent=2):
    for i in range(0,indent):
        print(" ",end="")
    print(cmd,end="")
    for i in range(0,cmdlen-len(cmd)):
        print(" ",end="")
    print(effe)

def know(namespace):
    words=read()
    if namespace.eng:
        idx=-1
        for i in range(0,len(words)):
            if namespace.eng==words[i][0]:
                idx=i
                break
        else:
            print(namespace.eng+" not found!",file=stderr)
            return
    else:
        try:
            with open(os.path.expanduser("~/.vocab/last_word.json"),"r") as f:
                idx=json.load(f)
        except:
            print("Can't fine the last word",file=stderr)
            exit()
    words[idx][2]*=0.9
    words[idx][2]+=0.1
    write(words)


def add(namespace):
    words=read()
    for word in words:
        if namespace.eng==word[0]:
            print(namespace.eng+" exists!")
            return
    words.append([namespace.eng,namespace.chi,0,1])
    write(words)
    try:
        with open(os.path.expanduser("~/.vocab/last_word.json"),"w") as f:
            json.dump((-1),f)
    except FileNotFoundError:
        pass

def version(namespace):
    import version
    print("version: alpha %d.%d.%d"% (version.major, version.minor, version.revision))
    print("last update", version.date)

def show(namespace):
    words=read()
    for word in words:
        display(word[0],word[1],indent=0)
    print(str(len(words))+" words in total!")

def get_word(namespace):
    try:
        with open(os.path.expanduser("~/.vocab/last_word.json"),"r") as f:
            i=json.load(f)
    except:
        i=0
    words=read()
    if i==-1:
        i=len(words)-1
    else:
        while True:
            i+=randint(0,len(words)-1)
            i%=len(words)
            if random()>words[i][2]:
                break
    word=words[i]
    display(word[0],word[1],indent=0)
    try:
        with open(os.path.expanduser("~/.vocab/last_word.json"),"w") as f:
            json.dump((i),f)
    except FileNotFoundError:
        pass

def init(namespace):
    print("Are you sure you want to initialize? ALL files will be cleared unless you backup them manually")
    print("""Input "Yes, I know exactly what I'm doing" to continue""")
    if input()=="Yes, I know exactly what I'm doing":
        words=[]
        write(words)
    else:
        print("Initialization canceled")

def remove(namespace):
    print(namespace)
    return
    words=read()
    if namespace.word:
        for i in range(0,len(words)):
            if words[i][0]==namespace.word or words[i][1]==namespace.word:
                del words[i]
                write(words)
                return
        print(namespace.word+" not found!")
    else:
        try:
            with open(os.path.expanduser("~/.vocab/last_word.json"),"r") as f:
                i=json.load(f)
        except:
            print("Can't fine the last word",file=stderr)
            exit()
        print("The last word is ",end="")
        display(words[i][0],words[i][1],indent=0)
        print("Would you like to delete it from the list?(y for yes)")
        if input() in {"y","yes"}:
            del words[i]
            write(words)
            return
        else:
            print("operation canceled!")
