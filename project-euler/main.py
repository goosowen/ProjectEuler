import logging.config
import os

from config import MAX_PROBLEMS
from runner import runner

logging.config.fileConfig(os.path.abspath(os.path.join('.', 'logging.conf')))
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    runner = runner.Runner(logger, MAX_PROBLEMS)
    runner.verify_all_solutions(parallel=False)
