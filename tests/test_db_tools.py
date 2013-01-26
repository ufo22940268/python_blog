import subprocess
import unittest

class DbToolsTest(unittest.TestCase):
    def test_not_valid(self):
        self.assertIn("Usage", self.invoke_with_param("dadsfadf"));

    def test_create_db(self):
        self.invoke_with_param("create");

    def test_update_db(self):
        self.assertIn("update_db", self.invoke_with_param("update"));

    def invoke_with_param(self, param):
        return subprocess.check_output(["python", "db_tools.py", param]);

if __name__ == "__main__":
    unittest.main();
