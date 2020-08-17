import requests


def canon(url: str, max_redirects=50, timeout=5):
	current_url = url
	viewed = []
	n = 0
	while n < max_redirects:
		n += 1
		viewed.append(current_url)
		print(current_url)
		with requests.get(current_url, allow_redirects=False, stream=True, timeout=timeout) as res:
			print('got response')
			print(f'first bytes: {str(res.raw.read(100))}')
			if res.status_code < 300 or res.status_code >= 400:
				return res.url, res
			else:
				new_url = res.headers['Location']
				if new_url in viewed:
					raise RuntimeError('Redirect cycle detected')
				current_url = new_url
	raise RuntimeError('Too many redirects')
