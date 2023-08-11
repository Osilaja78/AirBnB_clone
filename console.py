#!/usr/bin/python3
"""
The HBNBCommand class, a command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the HBNB command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF command to exit the porgram"""

        return True

    def do_emptyline(self):
        """Does nothing when an empty line is entered"""

        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
