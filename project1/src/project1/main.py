import loguru

logger = loguru.logger


def function1(a: int):
    logger.info(f"In function1 {a=}")
    return True


def function2(b: int):
    a = b + 1 + 1 + 1
    logger.info(f"In function2 {a=}")
    return True


if __name__ == "__main__":
    print("Hello, World!")
