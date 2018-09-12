import os
from importlib import import_module
from common.constants import VerificationType
import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("%r (%r, %r) %2.2f sec".format(method.__name__, args, kw, te - ts))
        return result

    return timed


def get_my_answer(problem_number):
    try:
        euler_file = "solvers.euler" + str(problem_number).zfill(3)
        mod = import_module(euler_file)
        met = getattr(mod, "main")
        return str(met())
    except Exception as e:
        print(e)
        return None


def get_solution(problem_number):
    script_dir = os.path.dirname(__file__)
    rel_path = "../solutions.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path) as f:
        for line in f.readlines():
            problem_and_solution = line.split('. ')
            if len(problem_and_solution) == 2:
                problem = int(problem_and_solution[0])
                if problem == problem_number:
                    solution = int(problem_and_solution[1].strip())
                    return solution

    return None


def verify_solution(problem_number, my_answer=None):
    if not my_answer:
        my_answer = get_my_answer(problem_number)

    if not my_answer:
        return VerificationType.exception

    if my_answer == "unimplemented":
        return VerificationType.unimplemented

    solution = get_solution(problem_number)
    if not solution:
        return VerificationType.unknown

    if my_answer == solution:
        return VerificationType.correct
    else:
        return VerificationType.incorrect
