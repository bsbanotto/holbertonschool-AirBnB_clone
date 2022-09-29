#!/usr/bin/python3
"""
This module contains the entry point for the command
interpreter.
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
valid_class = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    This class will implement the HBNB builtin Command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        quit command exits the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        Exits the application on End of File
        """
        raise SystemExit

    def emptyline(self):
        """
        When empty line, do nothing
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        Saves new instance to the JSON file
        Prints the id of the new instance
        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args in valid_class.keys():
            new = valid_class[args]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **

        If the id is missing, prints:
            ** instance id missing **

        If the instance of the class name doesn't exist for the id, prints:
            ** no instance found **
        """
        list_args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif list_args[0] in valid_class.keys():
            if len(list_args) == 1:
                print("** instance id missing **")
            else:
                obj_search = list_args[0] + "." + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    print(obj_all[obj_search])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        and saves change to the JSON file
        If the class name is missing, prints:
            ** class name missing **

        If the class name doesn't exist, prints:
            ** class doesn't exist **

        If the id is missing, prints:
            ** instance id missing **

        If the instance of the class name doesn't exist for the id, print:
            ** no instance found **
        """
        list_args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif list_args[0] in valid_class.keys():
            if len(list_args) == 1:
                print("** instance id missing **")
            else:
                obj_search = list_args[0] + "." + list_args[1]
                obj_all = storage.all()
                if obj_search in obj_all:
                    del obj_all[obj_search]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not
        on the class name.
        The printed result will be a list of strings
        If the class name doesn't exist, prints:
            ** class doesn't exist **
        """
        if len(args) == 0:
            for key in storage.all():
                print([str(storage.all()[key])])
        elif args not in valid_class.keys():
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args == value.__class__.__name__:
                    print([str(storage.all()[key])])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute(saved to the JSON file)
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()