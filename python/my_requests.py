import requests
from bs4 import BeautifulSoup

# 目標網址（你可以換成任何網站）
url = "https://en.wikipedia.org"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
# 發送 HTTP GET 請求
response = requests.get(url, headers=headers)

# 檢查請求是否成功
if response.status_code == 200:
    # 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 查找標題 (假設網站標題用 <h2> 標籤)
    titles = soup.find_all("h3")

    # 打印每個標題
    for title in titles:
        print(title.text.strip())
else:
    print(f"無法訪問網站，狀態碼: {response.status_code}")
