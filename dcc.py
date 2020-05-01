# usr/bin/python3
# Gabut gan hwhwhw
# Start: Fri May 01 2020,- 18:40:29 WIB
# Done : Fri May 01 2020,- 19:12:18 WIB
import requests as r
import re
from sys import argv

def ByPas(url):
	print('\n[÷] Bypasing => '+url)
	get_ = r.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
	if get_.status_code == 200:
		try:
			xe_ = re.search('<link \w+\=\"\w+" href\=\"(.*?)"',get_.text).group(1)
			if 'duit.cc' in xe_:
				_xi = re.search('rel\=\"noreferrer" href\=\"(.*?)"',get_.text).group(1).split('=')[1]
				print('[÷] Succses  => '+_xi)
			else:
				print('[÷] Succses  => '+xe_)
		except Exception as e:
			print('--eror-- => '+str(e))
	else:
		exit('[÷] Failed Bypasing => '+url)

if __name__ == "__main__":
	if len(argv) < 2:
		exit(f'Jalankan : python {argv[0]} <url>')
	else:
		ByPas(argv[1])
