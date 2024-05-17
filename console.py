#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        "handling quit command"
        return True

    def do_EOF(self, arg):
        "handling EOF"
        return True

    def help_quit(self):
        "help for quit command"
        print("Quit command to exit the program")

    def help_EOF(self):
        "help for EOF"
        print("EOF to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
