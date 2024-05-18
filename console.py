#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        else:
            try:
                my_instance = eval(arg)()
                my_instance.save()
                print(my_instance.id)
            except NameError:
                print("** class doesn't exist **")
                return
    def do_show(self, arg):
        arguments = arg.split()
        if not arguments:
            print("** class name missing **")
            return
        class_name = arguments[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        obj_id = arguments[1]
        key =" {}.{}".format(class_name,obj_id)
        objects_dict = storage.all()
        if key not in objects_dict:
            print("** no instance found **")
            return
        print(objects_dict[key])
                

if __name__ == '__main__':
    HBNBCommand().cmdloop()
