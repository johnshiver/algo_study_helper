"""
Takes all study logs and generates a single report page.
"""
from collections import namedtuple
import os

study_dir = ".study_logs/"
if not os.path.exists(study_dir):
    print("No study logs!")
    exit()

log_result = namedtuple("log_result", ['problem_name', 'passes', 'fails'])
final_results = []
all_logs = os.listdir(study_dir)
for log_file in all_logs:
    problem_name = log_file.replace(".log", "")
    passes, fails = 0, 0
    with open(study_dir + log_file, "r") as f:
        for line in f:
            if "Error" in line:
                fails += 1
            else:
                passes += 1
    result = log_result(problem_name=problem_name, passes=passes, fails=fails)
    final_results.append(result)

lines = "-" * 30
print("Test Results")
print(lines)
for result in final_results:
    print(result.problem_name.title() + "\n")
    print("Passes: " + str(result.passes))
    print("Fails: " + str(result.fails))
    print(lines)
