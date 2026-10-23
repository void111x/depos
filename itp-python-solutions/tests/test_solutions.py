"""Executable smoke tests plus independently specified expected answers and boundaries."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run(path, data=None):
    command = [sys.executable, str(ROOT / path)]
    if data is None:
        command.append('--demo')
    return subprocess.run(command, input=data, text=True, capture_output=True, timeout=15)


class SolutionsTest(unittest.TestCase):
    def test_all_219_scripts(self):
        records = json.loads((ROOT / 'manifest.json').read_text())
        self.assertEqual(len(records), 219)
        for record in records:
            with self.subTest(path=record['path']):
                result = run(record['path'])
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_known_answers(self):
        expected = {
            '01/practice_01': ['Python'], '01/practice_02': ['23'],
            '01/practice_03': ['95'], '01/practice_04': ['True'],
            '01/practice_05': ['12.5', '12'], '01/practice_06': ["<class 'str'>"],
            '01/practice_07': ['25'], '01/practice_08': ['20 10'],
            '01/practice_09': ['True'], '01/practice_10': ['98.6'],
            '02/practice_01': ['payable: 450.00'], '02/practice_02': ['60.00 km/h'],
            '02/practice_03': ['250.00', '405.00', '2655.00'],
            '02/practice_04': ['a/b = 6.25', 'a//b = 6'],
            '02/practice_05': ['16.00', '1680.00'],
            '02/practice_06': ['95.0', '[5]'],
            '02/practice_07': ['120000.00', '620000.00', '25833.33'],
            '02/practice_09': ['144.00', '1944.00', '486.00'],
            '02/practice_10': ['23.51', 'Normal'],
            '04/practice_02': ['1\n2\n3\n4\n5'],
            '04/practice_06': ['2\n4\n6\n8\n10'],
            '04/practice_07': ['24'], '04/practice_08': ['120'],
            '04/practice_09': ['0 1 1 2 3'],
            '04/practice_10': ['*\n**\n***'],
            '06/practice_03': ['[2 5]', 'Free slots: 13', '67.5'],
            '06/practice_05': ['[4]', 'Max stock: 30', '[[4 1]]'],
            '06/practice_06': ['250', '[[3 4]]', '[1]', '193.08333333333334'],
            '07/practice_01': ['Removed oldest: 1102', '[1215, 1045'],
            '07/practice_06': ['Highest: 95', 'Average: 85.75'],
            '07/practice_09': ['(10, 245)', '(8, 240)', '(9, 235)', '[3]'],
            '07/practice_10': ['A101 count: 2', 'C302 index: 7'],
            '08/practice_01': ['Present: 4'],
            '08/practice_06': ['Asha'], '08/practice_07': ['3'],
            '08/practice_08': ['0'], '08/practice_09': ['Ravi'],
            '09/practice_01': ['4.8', 'No warning'],
            '09/practice_02': ['23.51 Normal'], '09/practice_03': ['27'],
            '09/practice_04': ['2655.00'], '09/practice_05': ["('python makes ai easy', 4)"],
            '09/practice_06': ['8'], '09/practice_07': ['Hello Student'],
            '09/practice_08': ['24'], '09/practice_10': ['25'],
            '10/practice_02': ['STU2****1098'],
            '10/practice_03': ['Altitude: 250 Speed: 45 Battery: 78'],
            '10/practice_05': ['Fever: 3', 'Unique count: 4'],
            '10/practice_06': ['toPo'], '10/practice_07': ['DATA_SCIENCE'],
            '10/practice_08': ['NLP-DL-ML-AI'],
            '10/practice_09': ['Programming'], '10/practice_10': ['Python-makes-coding-easy'],
        }
        for short_path, answers in expected.items():
            with self.subTest(path=short_path):
                result = run('practical_' + short_path + '.py')
                self.assertEqual(result.returncode, 0, result.stderr)
                for answer in answers:
                    self.assertIn(answer, result.stdout)

    def test_boundary_inputs(self):
        cases = [
            ('01/main_04', '1\n2.5\nhello\nfalse\n', 'False'),
            ('01/main_09', 'hello\nworld\n', 'helloworld'),
            ('01/main_09', 'True\n2\n', 'Invalid combination'),
            ('02/main_02', '10\n0\n', 'Cannot divide by zero'),
            ('03/main_03', '90\n', '\nA\n'),
            ('03/main_03', '75\n', '\nB\n'),
            ('03/main_03', '50\n', '\nC\n'),
            ('03/main_05', '7 7 7\n', '[1, 2, 3]'),
            ('03/main_06', '1900\n', 'Not leap year'),
            ('03/main_06', '2000\n', 'Leap year'),
            ('03/main_08', '1000\n', 'payable: 900.00'),
            ('03/main_09', '1 2 3\n', 'Invalid triangle'),
            ('03/practice_02', '30000\n700\n', 'Rejected'),
            ('03/practice_03', '2000\n', 'final: 2000.00'),
            ('03/practice_03', '5000\n', 'final: 4500.00'),
            ('03/practice_05', '0\n', '0.00'),
            ('03/practice_05', '24\n', '100.00'),
            ('04/main_04', '0\n', 'for: 1 while: 1'),
            ('04/main_06', '0\n', 'Reverse: 0 Palindrome: True'),
            ('04/main_07', '0\n', 'Total: 1 Even: 1 Odd: 0'),
            ('04/main_08', '1\n', 'Not prime'),
            ('04/main_08', '2\n', 'Prime'),
            ('04/main_08', '49\n', 'Not prime'),
            ('05/main_04', '1 2 3\n9\n', 'Not found'),
            ('05/main_05', '101\n', 'No multiple'),
            ('05/main_07', '-4\n3\n2\n0\n', 'Sum: 5.0'),
            ('05/main_08', 'x\nx\nx\n', 'Access denied'),
            ('05/practice_05', '1\n2\n3\n4\n5\n', 'Locked after five failures'),
            ('06/main_04', '1\n2\n1 2\n3 4\n', '[[4.0, 6.0]]'),
            ('09/main_11', '2\n29\n', 'True'),
            ('10/main_11', 'A man, a plan, a canal: Panama\n', 'Palindrome: True'),
        ]
        for short_path, data, expected in cases:
            with self.subTest(path=short_path, data=data):
                result = run('practical_' + short_path + '.py', data)
                self.assertEqual(result.returncode, 0, result.stderr)
                # Interactive prompts have no newline before output.
                self.assertIn(expected.strip(), result.stdout)


if __name__ == '__main__':
    unittest.main()
