import time
from collections.abc import Callable


def retry(operation: Callable[[], object],
          attempts: int = 5,
          initial_delay: float = 2.0,
          max_delay: float = 60.0) -> object:
    delay = initial_delay

    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except TimeoutError:
            if attempt == attempts:
                raise

            time.sleep(min(delay, max_delay))
            delay *= 2

    raise RuntimeError("unreachable")
