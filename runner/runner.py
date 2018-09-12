import gevent.monkey
gevent.monkey.patch_all()
from gevent.pool import Group
from enum import Enum

# TODO cleanup and be more efficient about these imports
def get_my_answer(number):
    from importlib import import_module
    try:
        euler_file = "solvers.euler" + str(number).zfill(3)
        mod = import_module(euler_file)
        met = getattr(mod, "main")
        return str(met())
    except Exception as e:
        print(e)
        return None


class Runner:
    def __init__(self, logger, max_problems):
        self.logger = logger
        self.max_problems = max_problems

        self.problems = range(1, self.max_problems)
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.solutions = {}
        self.populate_solutions()

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

        self.logger.info('Solution to problem %s not found in problems.txt', num)
        return False

    def verify_all_solutions(self):
        verification_task_group = Group()
        tasks = []
        results = []

        for problem_number in self.problems:
            tasks.append(verification_task_group.spawn(self.verify_solution, problem_number))

        gevent.joinall(tasks)
        for task in tasks:
            if task.successful():
                results.append(task.value)
            else:
                raise ValueError('gevent thread was not successful')

        for r in results:
            if r:
                self.correct_answers += 1
            else:
                self.incorrect_answers += 1

        self.log_statistics()

    def verify_solution(self, number):
        my_answer = get_my_answer(number)
        if not my_answer or my_answer == "TODO":
            return

        solution = self.get_solution(number)
        if not solution:
            self.logger.warning("Solution doesn't exist for problem %s", number)
            return "Correct"

        if my_answer == solution:
            return True
        else:
            self.logger.warning("Incorrect answer to problem %s: %s", number, my_answer)
            return False

    def log_statistics(self):
        self.logger.info("CORRECT: %s", self.correct_answers)
        self.logger.info("INCORRECT: %s", self.incorrect_answers)
        self.logger.info("UNIMPLEMENTED: %s", self.max_problems - self.correct_answers - self.incorrect_answers)
