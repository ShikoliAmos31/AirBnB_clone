#!/usr/bin/python3
"""
Module for the HBNB command interpreter.
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

