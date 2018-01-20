# Algorithm Study Helper

A project intended to create a very productive practice work flow for
algorithms study.

The Algorithm Study Helper automatically generates practice problem files
and tests based on the problems defined in the problems directory. Test suite
results are logged to the .study_logs directory, and can be condensed into a
single report using the generate_study_report.py command.

This project has a directory of existing problems, but includes tools
to easily add your own.

**DISCLAIMER**

So far I have only tested this project with python 3.5, I am fairly sure
my insruction prompts will not execute using python 2.X, but otherwise the
code should mostly be compatible.

## Installation

There are no third party dependencies for this project, this is intentional :)

## Workflow

### Create a problem

'''
python3 create_problem_file.py
'''

Creates new problem file in problems dir, stubs out the data structures
you need to define in order to hook into go_study command properly.

INSTRUCTIONS should be a string, defining the instructions of the problem.

solution is a function that defines the ideal solution.

test_case_inputs should be all the inputs you want to study again.  the
auto-generated test cases simply send the test_inputs to both the ideal solution
and the user solution, comparing the two outputs for equality.

### Study problems

'''
python3 go_study.py
'''

The go_study command picks a random problem from the problems directory,
and generates scratch.py and test_scratch.py files (or overwrites them if
they already exist).  Your solution should be added to the main function
in scratch.py


### Test solution

'''
python3 test_scratch.py
'''

test_scratch.py runs the auto-generated test suite, and logs the results
to .study_logs/<problem_name>.log.


### See long term results

'''
python3 generate_study_report.py
'''

generate_study_report condenses all log files into a single readable display,
so you can get an idea of which problems you have trouble with / which ones
you should spend more time on.
