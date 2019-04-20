from include import *
from word import *
from random import randint
def add():
    words=read()
    words.append([argv[2],argv[3],0,1])
    write(words)

def version():
    print("version: beta")

def help():
    print("Usage: vocab <command>")
    print("Commands:")
    print("  word\t\t  Get one word(Default)")
    print("  show\t\t  Print all words on the vocabulary")
    print("  add <en> <ch>   Add a new word")
    #print("  init\t\tDo initialization")
    print("Options")
    print("  --version\t  Display version information")
    print("  --help\t  Display help information")

def show():
    words=read()
    for word in words:
        print(word[0]+"\t"+word[1]+"\t")

def get_word():
    words=read()
    i=randint(0,len(words))
    word=words[i]
    print(word[0]+"\t"+word[1]+"\t")


handler_dict={
    r"--version":version,
    r"--help":help,
    r"-h":help,
    r"help":help,
    r"show":show,
    r"add":add,
    r"word":get_word,
}
