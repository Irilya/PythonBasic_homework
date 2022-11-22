import requests
import re


link = 'http://www.columbia.edu/~fdc/sample.html'
result = requests.get(link)
text_pattern = re.compile(r'<h3.*>(.*)<.*h3>')

str_h3 = text_pattern.findall(result.text)

for item in str_h3:
    print(item)
