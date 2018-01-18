import os
import random

ESSENTIAL_DIRS = {
    "PROBLEM_FILES": "problems/",
    "STUDY_LOGS": ".study_logs/"
}


def initialize():
    for dir_ in ESSENTIAL_DIRS.values():
        if not os.path.exists(dir_) and os.path.isdir(dir_):
            os.makedirs(dir_)


def get_problem():
    problem_dir = ESSENTIAL_DIRS['PROBLEM_FILES']
    all_problems = os.listdir(ESSENTIAL_DIRS['PROBLEM_FILES'])

    # remove init file and all pyc files
    all_problems.remove("__init__.py")
    all_problems = filter(lambda x: x.endswith('.py'), all_problems)
    all_problems = [x.strip('.py') for x in all_problems]
    return problem_dir + random.choice(list(all_problems))


def generate_scratch_pad_and_test_file_from_problem_file(problem_file):
    from importlib import import_module

    imported_problem_path = problem_file.replace("/", ".")
    imported_problem = import_module(imported_problem_path)

    scratch_file_name = "scratch.py"
    test_file_name = "test_scratch.py"
    useful_files = [
        scratch_file_name,
        test_file_name
    ]
    # clear out old files
    for f in useful_files:
        if os.path.exists(f):
            os.remove(f)

    test_template = """import unittest

from scratch import main
from {} import solution

class MyTest(unittest.TestCase):
    """

    test_method = """
    def test{}(self):
        self.assertEqual(main({}), solution({}))
    """

    problem_template = """
'''
Instructions\n{}
'''

def main(args):
    # your code here
    """.format(imported_problem.INSTRUCTIONS)

    test_tail = """
if __name__ == '__main__':
    unittest.main()
    """

    test_template = test_template.format(imported_problem_path)
    for x, y in enumerate(imported_problem.test_case_inputs):
        test_template += test_method.format(x, y, y)

    test_template += test_tail
    with open(test_file_name, "w") as test_file:
        test_file.write(test_template)
    with open(scratch_file_name, "w") as scratch_file:
        scratch_file.write(problem_template)

    problem_name = imported_problem_path.lstrip("problems").replace(".", "")
    print("Now studying the {} problem".format(problem_name))


def main():
    initialize()
    curr_problem = get_problem()
    generate_scratch_pad_and_test_file_from_problem_file(curr_problem)

if __name__ == "__main__":
    main()
