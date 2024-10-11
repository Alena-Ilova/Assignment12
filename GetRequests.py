import requests
import re
import os
url = 'https://gsom.spbu.ru/en/'
response = requests.get(url)
if response.status_code == 200:
content = response.text

png_links = re.findall(r'https?://[^\s]+\.png', content)
png_count = len(png_links)
print(f"Number of links to png images: {png_count}")

first_png_match = re.search(r'(/[^"\s]+\.png)', content)  
if first_png_match:
      relative_png_link = first_png_match.group(1)
        full_png_link = f"https://gsom.spbu.ru{relative_png_link}"
print(f"First png image link: {full_png_link}")

import requests
r = requests.get('https://gsom.spbu.ru/templates/gsom/img/favicon.png')
file = open('/home/jovyan/python_logo.png', 'wb')
file.write(r.content)
print(r)