import subprocess
import sys
import unittest
from pathlib import Path


class TestHolaMundo(unittest.TestCase):
    def test_output(self):
        script = Path(__file__).resolve().parents[1] / "a.py"
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "hola mundo")


if __name__ == "__main__":
    unittest.main()
