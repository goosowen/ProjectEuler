from common.constants import VerificationType
from config import MAX_PROBLEMS
from common.shared_functions import display_percent


class Displayer():
    def __init__(self, logger):
        self.logger = logger

    ### TODO improve
    def display(self, results):
        msgs = []
        results = sorted(results, key=lambda r: r[0])

        last_name = ""
        start = 1
        for r in results:
            problem_number = r[0]
            result = r[1]
            if result == VerificationType.UNKNOWN or result == VerificationType.UNIMPLEMENTED:
                name = "UNKNOWN/UNIMPLEMENTED"
            else:
                name = result.name

            if (name != last_name or problem_number == len(results)-1) and last_name != "":
                if start == problem_number-1:
                    msgs.append("[{}]:{}".format(start, last_name))
                else:
                    msgs.append("[{}-{}]:{}".format(start, problem_number-1, last_name))
                start = problem_number

            last_name = name

        msg = '\n' + '\t'.join(msgs)
        self.logger.info(msg)

    def log_statistics(self, results):
        result_type_dict = {}
        for r in results:
            result_type_dict[r[1]] = result_type_dict.get(r[1], 0) + 1

        msgs = [""]
        for v in VerificationType:
            n = result_type_dict.get(v, 0)
            msgs.append(display_percent(v.name, n, MAX_PROBLEMS))

        msg = '\n'.join(msgs)
        self.logger.info(msg)

        # self.logger.info("INCORRECT: %s", incorrect_answers)
        # self.logger.info("UNIMPLEMENTED: %s", max_problems - self.correct_answers - self.incorrect_answers)