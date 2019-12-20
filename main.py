from include import *
import commands as cm
import argparse

def main():
    epilog='''
To load a existed word list, copy it to ~/.vocab/data.json
Format:
        [["intern", "扣押，拘留", 0, 1], ["sore", "\u75bc\u75db\u7684", 0, 1]]
(English,Chinese,two numbers for further consideration)
(The order of English and Chinese can be swaped)
bug/issue report to https://github.com/Michael1015198808/zsh-vocab
'''

    parser = argparse.ArgumentParser(
            description='zsh-vocab : a terminal word reciting program/plugin',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=epilog)
    parser.set_defaults(func=cm.get_word)
    #parser.add_argument("--version", action="version", version="0")
    subparsers = parser.add_subparsers(help='sub-command help')

    version_help = 'print current version'
    init_help = 'do initialization'
    show_help = 'print all words in wordlist'
    know_help = 'mark last word as known'
    add_help = 'add a new word'
    word_help = 'randomly print a word'
    remove_help = 'remove a word'

    subparsers.add_parser('version',   help=version_help).set_defaults(func=cm.version)
    subparsers.add_parser('init',      help=version_help).set_defaults(func=cm.init)
    subparsers.add_parser('show',      help=show_help).set_defaults(func=cm.show)
    subparsers.add_parser('word',      help=word_help).set_defaults(func=cm.get_word)

    parser_know = subparsers.add_parser('know',      help=know_help)
    parser_know.add_argument('eng', nargs='?',
            help='the word to mark as known')
    parser_know.set_defaults(func=cm.know)

    parser_add = subparsers.add_parser('add',       help=add_help)
    parser_add.add_argument('eng', help='English of the word')
    parser_add.add_argument('chi', help='Chinese of the word')
    parser_add.set_defaults(func=cm.add)

    parser_remove = subparsers.add_parser('remove',    help=remove_help)
    parser_remove.add_argument('word', nargs='?',
            help='the word to be removed. Both language is fine.\nempty to remove the last word')
    parser_remove.set_defaults(func=cm.remove)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)

if __name__ == "__main__":
    main()
