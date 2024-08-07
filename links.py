import requests



def get_anime():
	url = "https://api.createporn.com/post/collection?limit=10000&include=userLikes&images=1&views=1&likes=1&timespan=0&date=1&generator=1&generatorId=anime"

	params= {
'Host': 'api.createporn.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Origin': 'https://www.createhentai.com',
'DNT': '1',
'Sec-GPC': '1',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'cross-site',
'TE': 'trailers',
'x-origin': 'https://www.createhentai.com',
'If-None-Match': 'W/"7a0-Nbo+6AkPS1CpRhHfDweznxQH7Pk"',
'Referer': 'https://www.createhentai.com/',
'Priority': 'u=4',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
    }

	response = requests.get(url, headers=params)
	json = response.json()
	results = json["results"]
	return results


def get_porn():
	url = "https://api.createporn.com/post/collection?limit=10000&include=userLikes&images=1&views=1&likes=1&timespan=0&date=1"

	params= {
'Host': 'api.createporn.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Origin': 'https://www.createporn.com',
'DNT': '1',
'Sec-GPC': '1',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'cross-site',
'TE': 'trailers',
'x-origin': 'https://www.createporn.com',
'If-None-Match': 'W/"7a0-Nbo+6AkPS1CpRhHfDweznxQH7Pk"',
'Referer': 'https://www.createporn.com/',
'Priority': 'u=4',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
    }

	response = requests.get(url, headers=params)
	json = response.json()
	results = json["results"]
	return results


def get_furry():
	url = "https://api.createporn.com/post/collection?limit=10000&include=userLikes&images=1&views=1&likes=1&timespan=0&date=1"

	params= {
'Host': 'api.createporn.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br, zstd',
'Origin': 'https://www.createaifurry.com',
'DNT': '1',
'Sec-GPC': '1',
'Connection': 'keep-alive',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'cross-site',
'TE': 'trailers',
'x-origin': 'https://www.createaifurry.com',
'If-None-Match': 'W/"7a0-Nbo+6AkPS1CpRhHfDweznxQH7Pk"',
'Referer': 'https://www.createaifurry.com/',
'Priority': 'u=4',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
    }
	response = requests.get(url, headers=params)
	json = response.json()
	results = json["results"]
	return results

