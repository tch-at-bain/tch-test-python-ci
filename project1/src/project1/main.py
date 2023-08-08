import loguru

logger = loguru.logger


def function1():
    logger.info("In function1")
    return True


if __name__ == "__main__":
    print("Hello, World!")
