from tasks import add
import time

import logging

if __name__ == "__main__":
    import random
    logging.basicConfig()
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)


    while True:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        

        c = add.delay(a, b).get()
        logger.info(f'{a}+{b}={c}')

        t = random.randint(0, 3)
        logger.info(f'Sleeping for {t} seconds')
        time.sleep(t)