#!/usr/bin/python3
"""Entry point of command interpreter"""
import cmd
import sys
from models.engine.get_class import classes, console_methods
from models import storage


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
        self.non_interactive_check()
        pass

    def do_help(self, arg):
        """List available commands with
            help or detailed help with help <command>"""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")


    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        self.non_interactive_check()
        arguments = self.arg_string_parse(arg)
        if self.not_class(arguments["cls_name"]):
            return
        cls = classes[arguments["cls_name"]]
        new_obj = cls()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arg)
        if self.not_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        print(__objects[key])

    def do_destroy(self, arg):
        """
         Deletes an instance based on
         the class name and id (save the change into the JSON file).
         """
        self.non_interactive_check()
        args = self.arg_string_parse(arg)
        if self.not_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        del __objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arg)
        __objects = storage.all()
        list_print = []
        if args["cls_name"] is None:
            for item in __objects:
                str_print = "{}".format(__objects[item].__str__())
                list_print.append(str_print)
        else:
            if self.not_class(args["cls_name"]):
                return
            for item in __objects:
                if item.split(".")[0] == args["cls_name"]:
                    str_print = "{}".format(__objects[item].__str__())
                    list_print.append(str_print)
        print(list_print)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        and save the change into the JSON file

        You can assume the attribute name is valid (exists for this model)
        """
        self.non_interactive_check()
        args = self.arg_string_parse(arg)
        if self.not_class(args["cls_name"]):
            return
        if self.not_an_instance(args["cls_name"], args["inst_id"]):
            return
        if self.not_attribute(args["attr_name"]):
            return
        if self.not_value(args["attr_value"]):
            return
        key = "{}.{}".format(args["cls_name"], args["inst_id"])
        __objects = storage.all()
        setattr(__objects[key], args["attr_name"], args["attr_value"])

    @staticmethod
    def arg_string_parse(arguments):
        """
        Splits input string of arguments
        arg order determines type of argument
        and arguments are space delimited

        Expected order:
        0. class name
        1. instance id
        2. attribute name
        3. attribute value
        """
        arg_list = arguments.split()
        args = {}
        if len(arg_list) >= 1:
            args["cls_name"] = arg_list[0]
        else:
            args["cls_name"] = None
        if len(arg_list) >= 2:
            args["inst_id"] = arg_list[1]
        else:
            args["inst_id"] = None
        if len(arg_list) >= 3:
            args["attr_name"] = arg_list[2]
        else:
            args["attr_name"] = None
        if len(arg_list) >= 4:
            args["attr_value"] = arg_list[3]
        else:
            args["attr_value"] = None
        return args

    @staticmethod
    def not_class(cls_name):
        """checks if given valid class name
        print customized error messages

        Arg:
            -cls_name (str): class name argument to check
        """
        if cls_name is None:
            print("** class name missing **")
            return True
        if cls_name not in classes:
            print("** class doesn't exist **")
            return True
        return False

    @staticmethod
    def not_an_instance(cls_name, inst_id):
        """
        Checks if given valid instance id
        Prints customized error message if missing or invalid

        Args:
        - cls_name (str): class name
        - inst_id (str): instance id to be checked
        """
        if inst_id is None:
            print("** instance id missing **")
            return True
        key = "{}.{}".format(cls_name, inst_id)
        __objects = storage.all()
        if key not in __objects:
            print("** no instance found **")
            return True
        return False

    @staticmethod
    def not_attribute(attr_name):
        """
        Checks if given attribute name
        Prints customized error message if missing
        If exists, attr_name is assumed to be valid

        Args:
        - attr_name (str): atrribute name to be checked
        """
        if attr_name is None:
            print("** attribute name missing **")
            return True
        return False

    @staticmethod
    def not_value(attr_value):
        """
        Checks if given attribute value argument
        Prints  customized error message if missing
        If exists, attr_valid is assumed to be valid
        """
        if attr_value is None:
            print("** value missing **")
            return True
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
