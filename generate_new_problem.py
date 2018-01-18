import shutil
import sys

TEMPLATE_FILE = "helper_files/problem_template"
PROBLEMS_DIR = "problems/"


if __name__ == "__main__":

    if not len(sys.argv) == 2:
        raise ValueError("Must supply one CLI: <problem_name>")

    new_problem_file_name = sys.argv[1]
    if not type(new_problem_file_name) == str:
        raise ValueError("problem name must be a string!")
    if not new_problem_file_name.endswith(".py"):
        new_problem_file_name += ".py"
    new_problem_file_name = "{}{}".format(PROBLEMS_DIR, new_problem_file_name)

    shutil.copy2(TEMPLATE_FILE, new_problem_file_name)
