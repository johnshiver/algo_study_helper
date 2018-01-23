"""
Takes all study logs and generates a single report page.
"""
from collections import namedtuple
import os

study_dir = ".study_logs/"
if not os.path.exists(study_dir):
    print("No study logs!")
    exit()

log_result = namedtuple("log_result", ['problem_name', 'passes',
                                       'fails', 'days'])
final_results = []
all_logs = os.listdir(study_dir)
for log_file in all_logs:
    problem_name = log_file.replace(".log", "")
    passes, fails, days = 0, 0, []
    with open(study_dir + log_file, "r") as f:
        for line in f:
            days.append(line[:10])
            if "Error" in line:
                fails += 1
            else:
                passes += 1
    days = len(set(days))
    result = log_result(problem_name=problem_name, passes=passes,
                        fails=fails, days=days)
    final_results.append(result)

lines = "-" * 30
print("Study Stats")
print(lines)
for result in sorted(final_results, key=lambda x: x.days, reverse=True):
    print(result.problem_name.title())
    print(lines)
    print("Passes: " + str(result.passes))
    print("Fails: " + str(result.fails))
    print("Study days: " + str(result.days))
    print(lines)
