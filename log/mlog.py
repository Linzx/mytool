from datetime import datetime


LOG_INFO = 'INFO'
LOG_ERROR = 'ERROR'
LOG_WARNING = 'WARNING'
LOG_NOTIFY = 'NOTIFY'
LOG_DEBUG = 'DEBUG'
LOG_USER = 'USER'

log_level = 6


def get_time_stamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


def info_log(value):
    if log_level > 3:
        print("\033[37m[%s]%s\033[0m" % (get_time_stamp(), value))


def error_log(value):
    if log_level != 0:
        print("\033[31m[%s]%s\033[0m" % (get_time_stamp(), value))


def warning_log(value):
    if log_level > 1:
        print("\033[33m[%s]%s\033[0m" % (get_time_stamp(), value))


def debug_log(value):
    if log_level > 5:
        print("\033[34m[%s]%s\033[0m" % (get_time_stamp(), value))


def notify_log(value):
    if log_level > 2:
        print("\033[36m[%s]%s\033[0m" % (get_time_stamp(), value))


def user_log(value):
    if log_level > 4:
        print("\033[32m[%s]%s\033[0m" % (get_time_stamp(), value))


def mlog(log_type, value):
    switcher = {
        'INFO': info_log,
        'ERROR': error_log,
        'WARNING': warning_log,
        'DEBUG': debug_log,
        'NOTIFY': notify_log,
        'USER': user_log
    }
    return switcher[log_type](value)


test = "logtest"
mlog(LOG_INFO, "hello %s" % test)
mlog(LOG_ERROR, "hello %s" % test)
mlog(LOG_DEBUG, "hello %s" % test)
mlog(LOG_NOTIFY, "hello %s" % test)
mlog(LOG_USER, "hello %s" % test)
mlog(LOG_WARNING, "hello %s" % test)
mlog(LOG_DEBUG, "hello %s" % test)