import logging
from logging.handlers import RotatingFileHandler


def log(level, message):

    logger = logging.getLogger('app')

    #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        log_name = 'app.log'
        log_count = 2
        log_format = '%(asctime)s %(levelname)s %(module)s %(funcName)s-[%(lineno)d] %(message)s'
        log_level = logging.INFO
        max_bytes = 10 * 1024 * 1024
        handler = RotatingFileHandler(log_name, mode='a', maxBytes=max_bytes, backupCount=log_count)
        handler.setFormatter(logging.Formatter(log_format))
        logger.setLevel(log_level)
        logger.addHandler(handler)

    if level == 'info':
        logger.info(message)
    if level == 'error':
        logger.error(message)


def file_sync(msg):
    try:
        with open('{0}'.format(msg.get('file_name')), 'w') as f:
            f.writelines(msg.get('content'))
        send_data = {"jid": msg.get("jid"), "retcode": 0, "stdout": "{0} sync success".format(msg.get("file_name"))}
        log("info", "{0} 文件同步完成".format(msg.get('file_name')))
        return send_data
    except Exception as e:
        send_data = {"jid": msg.get("jid"), "retcode": 1,
                     "stderr": "{0} sync exception: {1}".format(msg.get("file_name"), e)}
        log("error", "{0} 文件同步异常, {1}".format(msg.get('file_name'), e))
        return send_data
