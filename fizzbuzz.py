from logger import logging

logger = logging.getLogger()


ERR_INVALID_TYPE = "Please input integers"
ERR_INVALID_RANGE = "Integers must be between 1 and 100"


class FizzBuzz:

    def __init__(self, start: int, end: int):
        try:
            # check for input type if not int raise ValueError
            self.start = int(start)
            self.end = int(end)
        except ValueError:
            raise ValueError(ERR_INVALID_TYPE)

        self.__validate_range()  # validate if integers are between 1-100

    def __validate_range(self):
        if not (1 <= self.start and self.start <= 100 and 1 <= self.end and self.end <= 100):
            raise ValueError(ERR_INVALID_RANGE)

    def run(self):
        min_range = min(self.start, self.end)
        max_range = max(self.start, self.end)

        result = []
        for num in range(min_range, max_range):
            output = f"{num}: "
            if num % 3 == 0:
                output += "fizz "
            if num % 5 == 0:
                output += "buzz "

            logger.info(output)
            result.append(output)

        return result
