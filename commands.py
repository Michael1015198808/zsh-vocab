from include import *
from word import *
from random import randint
def display(cmd,effe):
    print("  "+cmd,end="")
    for i in range(0,15-len(cmd)):
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
    display("add <en> <ch>"," Add a new word")
    display("init","Do initialization")
    print("Options")
    display("--version","Display version information")
    display("--help","Display help information")

def show():
    words=read()
    for word in words:
        print(word[0]+"\t"+word[1]+"\t")

def get_word():
    words=read()
    i=randint(0,len(words)-1)
    word=words[i]
    print(word[0]+"\t"+word[1]+"\t")

def init():
    print("Are you sure you want to initialize? ALL files will be cleared unless you backup them manually")
    print("""Input "Yes, I know exactly what I'm doing" to continue""")
    if input()=="Yes, I know exactly what I'm doing":
        words=[]
        write(words)
    else:
        print("Initialization canceled")

handler_dict={
    r"--version":version,
    r"--help":help,
    r"-h":help,
    r"help":help,
    r"init":init,
    r"show":show,
    r"add":add,
    r"word":get_word,
}
