#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by sending End of File"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it to JSON file, and prints the id"""
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
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id, and saves the change into the JSON file"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key in objs:
            objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        objs = storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        print([str(objs[obj]) for obj in objs if obj.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        objs[key].save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            count = len([obj for obj in storage.all().values() if obj.__class__.__name__ == arg])
            print(count)
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Retrieve all instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            objs = storage.all()[arg]
            print(objs)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on his ID with a dictionary"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            dic = eval(args[2])
            for k, v in dic.items():
                setattr(objs[key], k, v)
            objs[key].save()
        except:
            print("** invalid dictionary **")

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        cmd, arg, line = self.parseline(line)
        if cmd in {'show', 'destroy', 'update', 'count', 'all'}:
            cmd += ' ' + arg
            return self.onecmd(cmd)
        print("*** Unknown syntax:", line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()

