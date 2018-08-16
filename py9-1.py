from urllib.parse import urlparse

url = 'https://www.most.gov.tw/folksonomy/List?menu_id=ba3d22f3-96fd-4adf一a078-91a05b8f0166& filter_uid=none&listKeyword=SpageNum=2&pageSize=18&View_mode'

uc = urlparse(url)
print('NetLoc :', uc.netloc)
print('path :', uc.path)

q_cmds = uc.query.split('&')
print('Query Commands : ')
for cmd in q_cmds:
    print(cmd)
