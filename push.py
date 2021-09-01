import requests

title = input("请输入标题：")
content = input("请输入内容：")

def get_page(url):
    page = requests.get(url)
    page = page.content
    page = page.decode('utf-8')
    return  page

print(get_page('http://tdtt.top?alias=GVance&title='+title+'&content='+content))