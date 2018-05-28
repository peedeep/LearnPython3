#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime, timedelta, timezone


print(datetime.now())
print(type(datetime.now()))


dt = datetime(2018, 5, 26, 12, 20)
print(dt)
print(dt.timestamp())


t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))


cday = datetime.strptime('2018-5-26 12:13:59', '%Y-%m-%d %H:%M:%S')
print(cday)


now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))


now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now + timedelta(days=1))
print(now + timedelta(days=2, hours=12))


tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo2_dt)
