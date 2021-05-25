import logging
import time
from multiprocessing import Process


def cube(name):
    logging.info(f"process {name}: starting")
    time.sleep(7)
    for x in my_numbers:
        logging.info(f'{x} cube is {x**3}')
    logging.info(f"process {name}: finishing")


def is_even(name):
    logging.info(f"process {name}: starting")
    time.sleep(5)
    for x in my_numbers:
        if x % 2 == 0:
            logging.info(f'{x} is an even number')
    logging.info(f"process {name}: finishing")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    my_numbers = [3, 4, 5, 6, 7, 8]
    my_process1 = Process(target=cube, args=('cube',), daemon=False)
    my_process2 = Process(target=is_even, args=('is_even',))
    my_process1.start()
    my_process2.start()
    # my_process1.join()
    logging.info("Done")
