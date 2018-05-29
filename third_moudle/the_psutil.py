#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import psutil


print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())

for x in range(10):
	print(psutil.cpu_percent(interval=1, percpu=True))


print('物理内存', psutil.virtual_memory())
print('交换内存', psutil.swap_memory())
print('磁盘分区信息', psutil.disk_partitions())
print('磁盘使用情况', psutil.disk_usage('/'))
print('磁盘IO', psutil.disk_io_counters())
print('获取网络读写字节/包的个数', psutil.net_io_counters())
print('获取网络接口状态', psutil.net_if_stats())
print('获取网络连接信息', psutil.net_connections())
