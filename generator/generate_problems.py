import os
from config import MAX_PROBLEMS
import logging.config

logging.config.fileConfig(os.path.abspath(os.path.join('..', 'logging.conf')))
logger = logging.getLogger(__name__)

SOLVER_DIR = 'solvers_test'
PROBLEM_FILE = os.path.abspath(os.path.join('..', 'problems.txt'))
SOLVER_DIR = os.path.abspath(os.path.join('..', 'solvers'))


def main():
    # maps problem numbers to their text
    problem_texts = {}

    with open(PROBLEM_FILE) as f:
        last_line = 0
        last_problem = 0
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip().startswith("Problem"):
                next_line = lines[i+1]
                if next_line.startswith("========="):
                    if last_problem != 0:
                        problem_text = ''.join(lines[last_line:i-2])
                        problem_texts[last_problem] = problem_text

                    last_problem = int(line.split(' ')[1])
                    last_line = i+2

        problem_text = ''.join(lines[last_line:i-1])
        problem_texts[last_problem] = problem_text

    logger.info("Highest problem in problems.txt: %s", last_problem)

    for i in xrange(1, MAX_PROBLEMS):
        file_path = os.path.join(SOLVER_DIR, "euler" + str(i).zfill(3) + ".py")
        if not os.path.isfile(file_path) and i in problem_texts:
            problem_text = problem_texts[i]
            file_text = '\n'.join(['#!/usr/bin/env python', '# -*- coding: utf-8 -*-', '"""',
                                   'Project Euler Problem ' + str(i), '=======================',
                                   problem_text + '"""', '\n', 'def main():', '    return "TODO"', '\n',
                                   'if __name__ == "__main__":', '    print main'])

            with open(file_path, 'w') as file:
                file.write(file_text)
                logger.info("Created %s", file_path)


if __name__ == '__main__':
    main()



