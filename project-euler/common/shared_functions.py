import os
from importlib import import_module
from common.constants import VerificationType
import time
import sys


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("%r (%r, %r) %2.2f sec".format(method.__name__, args, kw, te - ts))
        return result

    return timed


def get_percent(x):
    return round(100 * float(x), 2)


def display_percent(name, numerator, denominator):
    percent = get_percent(numerator / float(denominator + sys.float_info.epsilon))
    return "{}: {}/{} = {}%".format(name, round(numerator, 2), round(denominator, 2), percent)


def get_my_answer(problem_number):
    try:
        euler_file = "solvers.euler" + str(problem_number).zfill(3)
        try:
            mod = import_module(euler_file)
        except:
            return "unimplemented"
        met = getattr(mod, "main")
        return str(met())
    except Exception as e:
        print(problem_number, e)
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
                    solution = str(problem_and_solution[1].strip())
                    return solution

    return None


def verify_solution_wrapper(problem_number):
    return problem_number, get_and_verify_solution(problem_number)


def get_and_verify_solution(problem_number):
    solution = get_solution(problem_number)
    if not solution:
        return VerificationType.UNKNOWN

    my_answer = get_my_answer(problem_number)
    if my_answer is None:
        return VerificationType.EXCEPTION

    if my_answer == "unimplemented":
        return VerificationType.UNIMPLEMENTED

    my_answer = str(my_answer)
    if my_answer == solution:
        return VerificationType.CORRECT
    else:
        return VerificationType.INCORRECT


def verify_solution(problem_number, my_answer):
    solution = get_solution(problem_number)
    if not solution:
        return VerificationType.UNKNOWN

    if my_answer is None:
        return VerificationType.EXCEPTION

    if my_answer == "unimplemented":
        return VerificationType.UNIMPLEMENTED

    my_answer = str(my_answer)
    if my_answer == solution:
        return VerificationType.CORRECT
    else:
        return VerificationType.INCORRECT
