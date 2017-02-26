import logging

def log_maker(write) :
    logging.basicConfig(filename='logs.log',filemode='w',datefmt='%d/%m/%Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',level=logging.DEBUG)
    logging.info(write)