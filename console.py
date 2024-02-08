#!/usr/bin/python3
"""
Module for the HBNB command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self):
        """
        Help message for quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Exits the program when EOF is reached (Ctrl+D).
        """
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Empty line method to do nothing.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel"]:  # Add other classes here
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:  # Add other classes here
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:  # Add other classes here
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        all_objs = storage.all()
        if not arg:
            print([str(obj) for obj in all_objs.values()])
        elif arg not in ["BaseModel"]:  # Add other classes here
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objs.items() if arg in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:  # Add other classes here
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

