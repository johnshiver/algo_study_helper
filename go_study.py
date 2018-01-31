import os
import random
import sys
# thanks SO for help on tracking unit test results in tearDown method
# https://stackoverflow.com/questions/4414234/getting-pythons-unittest-results-in-a-teardown-method

ESSENTIAL_DIRS = {
    "PROBLEM_FILES": "problems/",
    "STUDY_LOGS": ".study_logs/",
}


def initialize():
    for dir_ in ESSENTIAL_DIRS.values():
        if not os.path.exists(dir_):
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

    # TODO: these strings are super messy
    #       should probably just be templates

    test_template = """import datetime
import unittest
import os

from scratch import main
from {} import solution

errors = 0

class {}Test(unittest.TestCase):

    def tearDown(self):
        # records whether or not a test case resulted in failure
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure

        global errors

        if not ok:
            errors += 1

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
    """

    test_method = """
    def test{}(self):
        ans, e_time = main({})
        sol, e2_time = solution({})
        self.assertEqual(ans, sol)
        # normalize execution times
        e_time *= 100000000
        e2_time *= 100000000
        import math
        self.assertLess(e_time, e2_time*math.log(e2_time)*10)
    """

    problem_template = """
'''
Instructions\n{}
'''

from utils.decorators import time_this

@time_this
def main(args):
    # your code here
    return
    """.format(imported_problem.INSTRUCTIONS)

    test_tail = """
if __name__ == '__main__':
    try:
        unittest.main()
    finally:
        # log results of unittest
        log_file = '{}'
        with open(log_file, "a") as f:
            if errors:
                log_string = "Errors: " + str(errors)
            else:
                log_string = "Pass"
            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d-%H:%M:%S | ')
            f.write(now + log_string + '\\n')
    """

    problem_name = imported_problem_path.lstrip("problems").replace(".", "")
    print("Now studying the {} problem".format(problem_name))

    log_file_name = ".study_logs/" + problem_name + ".log"
    test_template = test_template.format(imported_problem_path,
                                         problem_name.title())
    for x, y in enumerate(imported_problem.test_case_inputs):
        test_template += test_method.format(x, y, y)

    test_template += test_tail.format(log_file_name)
    with open(test_file_name, "w") as test_file:
        test_file.write(test_template)
    with open(scratch_file_name, "w") as scratch_file:
        scratch_file.write(problem_template)


def main():
    initialize()
    if len(sys.argv) > 1:
        problem_file = sys.argv[1]
        if not os.path.exists("problems/" + problem_file + ".py"):
            raise ValueError("Problem: {} doesnt exist!".format(problem_file))
            exit()

        else:
            curr_problem = "problems/" + problem_file
    else:
        curr_problem = get_problem()

    generate_scratch_pad_and_test_file_from_problem_file(curr_problem)

if __name__ == "__main__":
    main()
