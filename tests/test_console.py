#!/usr/bin/python3
"""
This contains the class for the console test cases
"""
import unittest
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand_prompt(unittest.TestCase):
    """represents test case for HBNBCommand"""

    def test_prompt(self):
        """test cases for prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand().prompt)


class HBNBCommand_create(unittest.TestCase):
    """test cases for create command"""

    def test_missing_classes(self):
        """test cases for missing classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

    def test_class_nonexistent(self):
        """Test case where class name doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

    def test_class_exists(self):
        """Test case where class name exists (BaseModel)"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            self.assertEqual(str, type(cmd_output))

            """ Check if ID is printed"""
            instance_id = cmd_output.split()[-1]
            self.assertIn(instance_id, cmd_output)


class HBNBCommand_show(unittest.TestCase):
    """test cases for show command"""

    def test_class_missing(self):
        """checks if class exists"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

    def test_class_nonexistent(self):
        """tests for non existent classess types"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

    def test_id_missing(self):
        """tests for id not types"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

    def test_id_notfound(self):
        """test for invalid id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")

    def test_instance_valid(self):
        """tests if valid id is typed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            show_output = f.getvalue().strip()

            self.assertIn("BaseModel", show_output)
            self.assertIn(instance_id, show_output)


class HBNBCommand_destroy(unittest.TestCase):
    """test cases for destroy command"""

    def test_destroy_validinstance(self):
        """Test destroy with valid instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            cmd_output = f.getvalue().strip()
            instance_id = cmd_output.split()[-1]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel {instance_id}")
            destroy_output = f.getvalue().strip()
            self.assertEqual(destroy_output, "")

    def test_missing_class(self):
        """tests for missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class name missing **")

    def test_nonexistent_class(self):
        """tests for non existent class"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy SomeModel 1234-1234-1234")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")

    def test_id_missing(self):
        """test for missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** instance id missing **")

    def test_invalid_id(self):
        """tests for invalid id types"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** no instance found **")


class HBNBCommand_all(unittest.TestCase):
    """test cases for all commmand"""

    def test_class_typed(self):
        """tests if a class is typed"""
        HBNBCommand().onecmd("create User")
        HBNBCommand().onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            all_output = f.getvalue().strip()

            self.assertTrue("[BaseModel]" in all_output)
            self.assertTrue("'created_at':" in all_output)
            self.assertTrue("'id':" in all_output)
            self.assertTrue("'updated_at':" in all_output)

    def test_class_missing(self):
        """tests if the class is missing"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all SomeModel")
            error_output = f.getvalue().strip()
            self.assertEqual(error_output, "** class doesn't exist **")


class HBNBCommand_quit(unittest.TestCase):
    """test cases for quit command"""

    def test_quit(self):
        """tests for quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
            self.assertEqual(f.getvalue().strip(), "")


class HBNBCommand_EOF(unittest.TestCase):
    """represents test cases for EOF command"""

    def test_EOF(self):
        """test cases for   EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))
            self.assertEqual(f.getvalue().strip(), "")


class HBNBCommand_emptyline(unittest.TestCase):
    """represents test cases for emptyline"""

    def test_emptyline(self):
        """test cases for emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue().strip(), "")


class HBNBCommand_default(unittest.TestCase):
    """test cases for default command"""

    def test_invalid_cmd(self):
        """test cases for invalid commad"""
        with patch('sys.stdout', new=StringIO()) as f:
            uk = "jkj"
            HBNBCommand().onecmd(uk)
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: {}".format(uk))

    def test_default_all(self):
        """test default all usage"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_var = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output[0], "[")
            self.assertEqual(output[-1], "]")
            self.assertTrue(id_var in output)

    def test_default_show(self):
        """tests default show usage"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id_var = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(id_var))
            output = f.getvalue().strip()
            self.assertTrue(id_var in output)
            self.assertTrue(output.startswith("[BaseModel]"))
            self.assertIn("datetime", output)
            self.assertIn("updated_at", output)
            self.assertIn("created_at", output)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show()')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("135)')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            storage_cpy = FileStorage()
            all_objs = len(storage_cpy.all())
            HBNBCommand().onecmd('BaseModel.destroy("{}")'.format(id_var))
            self.assertEqual(len(storage_cpy.all()), all_objs - 1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy()')
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("135)')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")


class TestHBNBCommand_help(unittest.TestCase):
    """unittest for testing the help me for each of the command"""

    def test_help_quit(self):
        """Test cases for help quit command"""
        quit_help = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(quit_help, f.getvalue().strip())

    def test_help_eof(self):
        """test cases for help eof command"""
        eof_help = "ctrl+D to exit the program"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(eof_help, f.getvalue().strip())

    def test_help_create(self):
        """test cases for help eof command"""
        create_help = "creates the instance of the variable"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(create_help, f.getvalue().strip())

    def test_help_update(self):
        """test case for the helf update command"""
        update_help = "updates an attribute in an object"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(update_help, f.getvalue().strip())

    def test_help_destroy(self):
        """test case for the helf destroy command"""
        destroy_help = "destroys an object from the json database"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(destroy_help, f.getvalue().strip())

    def test_help_count(self):
        """test case for the helf count command"""
        count_help = "counts the number of intsnaces of an object"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(count_help, f.getvalue().strip())

    def test_help_show(self):
        """test case for the helf destroy command"""
        show_help = "shows the object based on id"
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(show_help, f.getvalue().strip())

    def test_help(self):
        """Test case for the help command itself"""
        c = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(c, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
