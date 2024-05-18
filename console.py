#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """command interpreter using cmd methods"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command exit the program"""
        return True

    def do_EOF(self, arg):
        """ EOF command exit the program"""
        self.non_interactive_check()
        return True

    @staticmethod
    def non_interactive_check():
        if sys.stdin.isatty() is False:
            print("")

    def emptyline(self):
        """Do nothing on emty line inputs"""
        self.non_interactive_check
        pass

    def do_help(self, arg):
        """List available commands with
            "help" or detailed help with "help <command>"""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
