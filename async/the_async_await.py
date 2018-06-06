#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio


async def hello():
	print('hello world')
	r = await asyncio.sleep(1)
	print('hello again')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
#loop.close()

print('do next...')
#loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

