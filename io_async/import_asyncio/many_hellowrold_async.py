#!/usr/bin/env python3
# *-* coding: utf-8 *-*
import threading
import asyncio

@asyncio.coroutine
def hello():
	print("hello world (%s)" % threading.currentThread().getName())
	yield from asyncio.sleep(5)
	print("hello again (%s)" % threading.currentThread().getName())
	
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
