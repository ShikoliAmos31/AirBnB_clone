#!/usr/bin/python3
"""This module contains the entry point of the command interpreter."""
import cmd
import sys
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_EOF(self, line):
        """Exit the program."""
        print()
        return True

    def do_quit(self, line):
        """Quit the program."""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = arg.split()
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(value) for key, value in storage.all().items()
                       if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            class_id = args[1]
            key = "{}.{}".format(class_name, class_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            obj = storage.all()[key]
            setattr(obj, attr_name, attr_value)
            obj.save()
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")

    def default(self, line):
        """Default message."""
        print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """Count instances of a class."""
        try:
            class_name = eval(arg).__name__
            print(len([value for key, value in storage.all().items()
                       if key.startswith(class_name)]))
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representation of all instances."""
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            try:
                class_name = eval(arg).__name__
                print([str(value) for key, value in storage.all().items()
                       if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

