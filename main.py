from include import *
import commands as cm

try:
    os.mkdir(os.path.expanduser("~/.vocab"))
except FileExistsError:
    pass

try:
    with open(os.path.expanduser("~/.vocab/data.json"),"r") as f:
        try:
            words=json.load(f)
        except json.decoder.JSONDecodeError:
            words=[]
except FileNotFoundError:
    print(os.path.expanduser("~/.vocab/data.json"+" is not found."),file=stderr)
    print("call "+argv[0]+" help for more information",file=stderr)
    exit()

if len(argv)==1:
    cm.get_word()
else:
    try:
        handler=cm.handler_dict[argv[1]]
        handler()
    except KeyError:
        print("Unknown command "+argv[1],file=stderr)
        print("Use --help to use more information",file=stderr)
    pass

exit()
