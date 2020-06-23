import logging
import logging.handlers
import datetime

# 实例化logger
logger = logging.getLogger('mylogger')
# 设置logger的日志级别
logger.setLevel(logging.DEBUG)

# 设置一个按时间切割的处理器，在午夜的时间进行日志切割，将日志记录输出到all.log
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
# 为处理器设置一个格式器对象
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# 设置一个把日志输出到本地磁盘文件error.log的处理器
f_handler = logging.FileHandler('error.log')
# 设置处理器的级别为ERROR
f_handler.setLevel(logging.ERROR)
# 为处理器设置一个格式器对象
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

# 将两个处理器添加日志器上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')