import logging


# logging.basicConfig(level=logging.DEBUG)
# logging.debug('debug description')
# logging.info('info description')
# logging.warning('warning description')
# logging.error('error description')
# logging.critical('critical description')



logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='w')
formate = "We have next logging message:%(asctime)s:%(levelname)s - %(message)s"



try:
    print(10/0)
except Exception:
    logging.exception("Exception")
