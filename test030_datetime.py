from datetime import datetime, timezone, timedelta

# 获取当前日期和时间
now = datetime.now()
print('当前时间%s 类型%s' % (now, type(now)))
# 获取指定日期和时间
dt = datetime(2015, 2, 12, 10, 30, 31)
print(dt)
# 转换为timestamp
dts = dt.timestamp()
print('时间戳：', dts)
# 时间戳转换为时间
t = 1429417200.0
# 本地时间
dt2 = datetime.fromtimestamp(t)
print(dt2)
# UTC时间
dt_utc = datetime.utcfromtimestamp(t)
print(dt_utc)


# str转换为datetime


# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：
def to_timestamp(dt_str, tz_str):
    # 首先dt_str转换为datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 创建时区
    utc=timezone(timedelta(hours=int(tz_str.split(":")[0][3:])))
    dt2=dt.replace(tzinfo=utc)
    return dt2.timestamp()
    pass


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
