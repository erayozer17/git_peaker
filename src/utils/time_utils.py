from datetime import datetime, timedelta


def get_now_isoformat(sanitized=False):
    now = datetime.now().isoformat()
    if sanitized:
        return sanitize_isoformat_time(now)
    return now


def get_now():
    return datetime.now()


def get_time_days_before(days):
    delta_time = (get_now() - timedelta(days=days)).isoformat()
    return sanitize_isoformat_time(delta_time)


def sanitize_isoformat_time(time):
    return time.split(".")[0] + "Z"
