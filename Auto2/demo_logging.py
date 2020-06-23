import logging

logging.basicConfig(filename="爸爸.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# import logging
#
# logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
# a = 5
# b = 0
# try:
#     c = a / b
# except Exception as e:
#     # 下面三种方式三选一，推荐使用第一种
#     # logging.exception("Exception occurred")
#     # logging.error("Exception occurred", exc_info=True)
#     logging.log(level=logging.CRITICAL, msg="Exception occurred", exc_info=True)

a=10
logging.info("目前a的值为%d"%a)