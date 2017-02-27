import logging.config
import os
from importlib import import_module
from config import MAX_PROBLEMS

# TODO idk why it think I'm in the above directory already
logging.config.fileConfig(os.path.abspath(os.path.join('.', 'logging.conf')))
logger = logging.getLogger(__name__)


class Runner:

    def __init__(self):
        self.correct_answers = 0
        self.incorrect_answers = 0

        self.solutions = {}
        self.populate_solutions()

        self.problems = range(1, MAX_PROBLEMS)


    def populate_solutions(self):
        with open('solutions.txt') as f:
            for line in f.readlines():
                problem_and_solution = line.split('. ')
                if len(problem_and_solution) == 2:
                    problem = problem_and_solution[0]
                    solution = problem_and_solution[1].strip()
                    self.solutions[int(problem)] = solution

    def get_solution(self, num):
        if num in self.solutions:
            return self.solutions[num]

        logger.info('Solution to problem %s not found in problems.txt', num)
        return False

    def verify_all_solutions(self):
        for problem_number in self.problems:
            self.verify_solution(problem_number)

        self.log_statistics()

    def verify_solution(self, number):
        my_answer = self.get_my_answer(number)
        if not my_answer or my_answer == "TODO":
            return

        solution = self.get_solution(number)
        if not solution:
            logger.warning("Solution doesn't exist for problem %s", number)
            return

        if my_answer == solution:
            self.correct_answers += 1
        else:
            logger.warning("Incorrect answer to problem %s: %s", number, my_answer)
            self.incorrect_answers += 1

    def log_statistics(self):
        logger.info("CORRECT: %s", self.correct_answers)
        logger.info("INCORRECT: %s", self.incorrect_answers)
        logger.info("UNIMPLEMENTED: %s", MAX_PROBLEMS - self.correct_answers - self.incorrect_answers)

    # TODO cleanup and be more efficient about these imports
    def get_my_answer(self, number):
        try:
            euler_file = "solvers.euler" + str(number).zfill(3)
            mod = import_module(euler_file)
            met = getattr(mod, "main")
            return str(met())
        except Exception:
            return None

def main():
    runner = Runner()
    runner.verify_all_solutions()

if __name__ == '__main__':
    main()

