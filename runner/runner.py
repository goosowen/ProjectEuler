import gevent.monkey
from gevent.pool import Group
from runner.displayer import Displayer
from common.shared_functions import get_my_answer
from common.shared_functions import verify_solution
from common.constants import answer_types

gevent.monkey.patch_all()


class Runner:
    def __init__(self, logger, max_problems):
        self.logger = logger
        self.max_problems = max_problems

        self.problems = range(1, self.max_problems)
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.solutions = {}
        self.populate_solutions()

        self.displayer = Displayer()

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
            tasks.append(verification_task_group.spawn(verify_solution, problem_number))

        gevent.joinall(tasks)
        for task in tasks:
            if task.successful():
                results.append(task.value)
            else:
                raise ValueError('gevent thread was not successful')

        self.displayer.display(results)
