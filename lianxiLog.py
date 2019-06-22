import logging

class Logger():
    def __init__(self,path,CmdLevel,FileLevel):
        # 创建logger
        self.logger = logging.getLogger(path)
        # 设置默认log级别
        self.logger.setLevel(logging.DEBUG)
        # 定义输出handler的格式
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # 借助Handler将日志输出到日志文件中
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)  # 配置log
        fh.setLevel(FileLevel)
        # 创建一个handler,将日志输出到控制台上
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)  # 配置log
        sh.setLevel(CmdLevel)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)

if __name__ == '__main__':
    logger = Logger('logging.log',CmdLevel=logging.DEBUG,FileLevel=logging.ERROR)
    logger.debug("debug message")
    logger.info("info message")
    logger.warn("warning message")
    logger.error("error message")
    logger.cri("critical message")
