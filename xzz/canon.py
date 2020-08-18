import asyncio

import requests
import aiohttp


async def on_request_start(session, trace_config_ctx, params):
	print("Starting request", params, '\n-----')

async def on_request_end(session, trace_config_ctx, params):
    print("Ending request", params, '\n-----')

async def on_request_redirect(session, trace_config_ctx, params):
    print("Redirect", params, '\n-----')

async def on_connection_reuseconn(session, trace_config_ctx, params):
    print("Connection reused", params, '\n-----')

async def canon(url: str, timeout=5):
	trace_config = aiohttp.TraceConfig()
	trace_config.on_request_start.append(on_request_start)
	trace_config.on_request_redirect.append(on_request_redirect)
	trace_config.on_request_end.append(on_request_end)
	trace_config.on_connection_reuseconn.append(on_connection_reuseconn)

	async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
		async with session.get(url, allow_redirects=True, timeout=timeout) as res:
			return res.url, (await res.text())

	# current_url = url
	# viewed = []
	# n = 0
	# while n < max_redirects:
	# 	n += 1
	# 	viewed.append(current_url)
	# 	print(current_url)
	# 	async with aiohttp.ClientSession() as session:
	# 		async with session.get(current_url, allow_redirects=False, timeout=timeout) as res:
	# 			print('got response')
	# 			# print(f'first bytes: {str(res.raw.read(100))}')
	# 			if res.status < 300 or res.status >= 400:
	# 				return current_url, res
	# 			else:
	# 				new_url = res.headers['Location']
	# 				if new_url in viewed:
	# 					raise RuntimeError('Redirect cycle detected')
	# 				current_url = new_url
	# raise RuntimeError('Too many redirects')
