"""Demo of integrating a PythonTA check into a test suite.
"""
import contextlib
import io
import unittest

import python_ta


class TestFileWithPythonTa(unittest.TestCase):
    MODULE = 'demo2_style_checks.py'
    longMessage = False  # Make assertion error custom messages replace standard messages

    def test_file(self):
        """Check my_file.py with PythonTA."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            reporter = python_ta.check_all(self.MODULE,
                config={
                    'output-format': 'python_ta.reporters.PlainReporter'
                }
            )

        # Check that the file was successfully analysed
        self.assertIn(self.MODULE, reporter.messages, f'PythonTA did not run successfully on {self.MODULE}')

        # Access the messages reported by PythonTA
        messages = reporter.messages[self.MODULE]
        self.assertEqual(
            len(messages), 0,
            f'PythonTA detected {len(messages)} issue(s) in {self.MODULE}. PythonTA report:\n\n{buffer.getvalue()}'
        )


if __name__ == '__main__':
    unittest.main()
