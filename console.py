#!/usr/bin/python3
"""
Entry point of AirBnB project
"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    "entry point of the command interpreter"
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

    def emptyline(self):
        "do nothing on empty line"
        pass

    def do_create(self, arg):
        "creates a new instance"
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
        "prints string representation of an instance"
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
        key = " {}.{}".format(class_name,obj_id)
        objects_dict = storage.all()
        if key not in objects_dict:
            print("** no instance found **")
            return
        print(objects_dict[key])
                
    def do_destroy(self, arg):
        "deletes an instance"
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
        del objects_dict[key]
        storage.save()

    def do_all(self, arg):
        "prints all string representations of all instances"
        arguments = arg.split()
        class_name = arguments[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        objects_dict = storage.all()
        for key, value in objects_dict.items():
            class_name, obj_id = key.split('.')
            if class_name == arguments[0]:
                print (objects_dict[key])

    def do_update(self, arg):
        "updates an instance based on class name and id"
        arguments = arg.split()
        if len(arguments) == 0:
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
        key = " {}.{}".format(class_name,obj_id)
        objects_dict = storage.all()
        if key not in objects_dict:
            print("** no instance found **")
            return
        if len(arguments) == 2:
            print("** attribute name missing **")
            return
        attr = arguments[2]
        if len(arguments == 3):
            print("** value missing **")
            return
        val = arguments[3]
        attr_type = type(objects_dict[key][attr])
        try:
            casted_val = attr_type(val)
        except ValueError:
                pass
        objects_dict[key][attr] = casted_val
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
