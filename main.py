from logger import logging
from fizzbuzz import FizzBuzz

logger = logging.getLogger()


def main():
    try:
        start = input("Input integer (1-100): ")
        end = input("Input integer (1-100): ")
        FizzBuzz(start, end).run()
    except ValueError as err:
        logger.error(err)


if __name__ == "__main__":
    main()
