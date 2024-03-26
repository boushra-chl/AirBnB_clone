#!/usr/bin/python3
""" module that contains the entry point of the command interpreter"""


import cmd

class HBNBCommand(cmd.Cmd):
    """entry point class"""

    prompt = "(hbnb) "
    def do_help(self, arg):
        return super().do_help(arg)

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("handling end of file")

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
