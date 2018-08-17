# 要獲取 github 的公共時間線
import requests

r = requests.get('http://github.com/timeline.json')
print(r.text)
