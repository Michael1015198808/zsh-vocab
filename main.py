from include import *
import commands as cm

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
