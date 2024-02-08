#!/usr/bin/python3
import cmd
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it (to the JSON file) and print the id."""
        if not line:
            print("** class name missing **")
            return
        if line not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(line)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = line.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[obj]) for obj in all_objs])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(all_objs[obj]) for obj in all_objs if obj.startswith(args[0] + ".")])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        all_objs[key].save()

    def default(self, line):
        """Called on an input line when the command prefix is not recognized."""
        cmd, args, line = self.parseline(line)
        if '.' in cmd:
            class_name, action = cmd.split('.', 1)
            if action == "all()":
                self.do_all(class_name)
                return
            elif action == "count()":
                self.do_count(class_name)
                return
        print("*** Unknown syntax:", line)

    def do_create(self, line):
        """Creates a new instance of a class."""
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Shows the string representation of an instance based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances."""
        args = line.split()
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[obj]) for obj in all_objs])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(all_objs[obj]) for obj in all_objs if obj.startswith(args[0] + ".")])

    def do_count(self, class_name):
        """Retrieves the number of instances of a class."""
        all_objs = storage.all()
        count = sum(1 for obj in all_objs.values() if type(obj).__name__ == class_name)
        print(count)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(all_objs[key], args[2], args[3])
        all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

