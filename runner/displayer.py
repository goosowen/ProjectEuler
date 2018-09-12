class Displayer():
    def __init__(self, logger):
        self.logger = logger

    def display(self, results):
        self.logger.info(results)

    def log_statistics(self):
        self.logger.info("CORRECT: %s", self.correct_answers)
        self.logger.info("INCORRECT: %s", self.incorrect_answers)
        self.logger.info("UNIMPLEMENTED: %s", self.max_problems - self.correct_answers - self.incorrect_answers)