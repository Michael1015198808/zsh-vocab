from include import *
import commands as cm
import argparse

def main():
    parser = argparse.ArgumentParser(
            description='a terminal word reciting program/plugin',
            epilog="bug/issue report to https://github.com/Michael1015198808/zsh-vocab")
    parser.set_defaults(func=cm.get_word)
    #parser.add_argument("--version", action="version", version="0")
    subparsers = parser.add_subparsers(help='sub-command help')

    subparsers.add_parser('--version', help='').set_defaults(func=cm.version)
    subparsers.add_parser('show',      help='').set_defaults(func=cm.show)
    subparsers.add_parser('know',      help='').set_defaults(func=cm.know)
    subparsers.add_parser('add',       help='').set_defaults(func=cm.add)
    subparsers.add_parser('word',      help='').set_defaults(func=cm.get_word)
    subparsers.add_parser('remove',    help='').set_defaults(func=cm.remove)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func()
    exit()
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

    pass

if __name__ == "__main__":
    main()
