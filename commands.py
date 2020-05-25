from include import *
from word import *
from random import randint
def display(cmd,effe,cmdlen=15,indent=2):
    for i in range(0,indent):
        print(" ",end="")
    print(cmd,end="")
    for i in range(0,cmdlen-len(cmd)):
        print(" ",end="")
    print(effe)

def add():
    words=read()
    words.append([argv[2],argv[3],0,1])
    write(words)

def version():
    print("version: beta")

def help():
    print("Usage: vocab <command>")
    print("Commands:")
    display("word", "Get one word(Default)")
    display("show", "Print all words on the vocabulary")
    display("add <en> <ch>","Add a new word")
    display("init","Do initialization")
    display("rm <en>|<ch>","Remove a word from list(Default: the last word)")
    print("Options")
    display("--version","Display version information")
    display("--help","Display help information")
    print(r"To load a existed word list, copy it to ~/.vocab/data.json")
    print('''Format:
        [["intern", "扣押，拘留", 0, 1], ["sore", "\u75bc\u75db\u7684", 0, 1]]
(English,Chinese,two numbers for further consideration)
(The order of English and Chinese can be swaped)''')

def show():
    words=read()
    for word in words:
        display(word[0],word[1],indent=0)

def get_word():
    try:
        with open(os.path.expanduser("~/.vocab/last_word.json"),"r") as f:
            i=json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        i=0
    words=read()
    if words == []:
        print("No words in current vocabulary list!", file = stderr)
        exit()
    i+=randint(0,len(words)-1)
    i%=len(words)
    word=words[i]
    display(word[0],word[1],indent=0)
    try:
        with open(os.path.expanduser("~/.vocab/last_word.json"),"w") as f:
            json.dump((i),f)
    except FileNotFoundError:
        pass

def init():
    print("Are you sure you want to initialize? ALL files will be cleared unless you backup them manually")
    print("""Input "Yes, I know exactly what I'm doing" to continue""")
    if input()=="Yes, I know exactly what I'm doing":
        words=[]
        write(words)
    else:
        print("Initialization canceled")

def remove():
    words=read()
    if len(argv)==3:
        for i in range(0,len(words)):
            if words[i][0]==argv[2] or words[i][1]==argv[2]:
                del words[i]
                write(words)
                return
        print(argv[2]+" not found!")
    else:
        try:
            with open(os.path.expanduser("~/.vocab/last_word.json"),"r") as f:
                i=json.load(f)
        except:
            print("Can't fine the last word",file=stderr)
            exit()
        print("The last word is",end="")
        display(words[i][0],words[i][1],indent=0)
        print("Would you like to delete it from the list?(y for yes)")
        if input()=="y":
            del words[i]
            write(words)
            return
        else:
            print("operation canceled!")
handler_dict={
    r"--version":version,
    r"--help":help,
    r"-h":help,
    r"help":help,
    r"init":init,
    r"show":show,
    r"add":add,
    r"word":get_word,
    r"rm":remove,
    r"remove":remove,
}
