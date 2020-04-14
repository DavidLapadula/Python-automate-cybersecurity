import logging, os
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

def factorial(n): 
    logging.debug("Debug Start factorial(%s)" % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))
    logging.info("Return is %s" % (total))
    return total


logging.debug("Start Program")
factorial(5)
logging.debug("End Program")

