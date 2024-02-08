import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

class TestConsole(unittest.TestCase):
    """Test cases for console.py"""

    def setUp(self):
        """Set up test environment"""
        self.console = os.path.join(os.getcwd(), "console.py")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip() != "")
            HBNBCommand().onecmd("create User")
            self.assertTrue(f.getvalue().strip() != "")
            HBNBCommand().onecmd("create State")
            self.assertTrue(f.getvalue().strip() != "")

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            HBNBCommand().onecmd("show BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output.split()[-1][1:-1]
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            self.assertTrue(f.getvalue().strip() != "")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            HBNBCommand().onecmd("destroy BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output.split()[-1][1:-1]
            HBNBCommand().onecmd(f"destroy BaseModel {instance_id}")
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual(f.getvalue().strip(), "[]")
            HBNBCommand().onecmd("all BaseModel")
            self.assertEqual(f.getvalue().strip(), "[]")
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output.split()[-1][1:-1]
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(f.getvalue().strip() != "")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue().strip(), "0")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("count BaseModel")
            self.assertEqual(f.getvalue().strip(), "3")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            HBNBCommand().onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output.split()[-1][1:-1]
            HBNBCommand().onecmd(f"update BaseModel {instance_id}")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")
            HBNBCommand().onecmd(f"update BaseModel {instance_id} name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")
            HBNBCommand().onecmd(f"update BaseModel {instance_id} name John")
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            self.assertIn("John", f.getvalue().strip())

    def test_update_with_dictionary(self):
        """Test update with dictionary command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")
            HBNBCommand().onecmd("update BaseModel 12345")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            instance_id = output.split()[-1][1:-1]
            HBNBCommand().onecmd(f"update BaseModel {instance_id} {{}}")
            self.assertEqual(f.getvalue().strip(), "** invalid dictionary **")
            HBNBCommand().onecmd(f"update BaseModel {instance_id} {{name: John}}")
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            self.assertIn("John", f.getvalue().strip())

if __name__ == "__main__":
    unittest.main()

