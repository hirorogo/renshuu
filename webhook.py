import requests
from lxml import html

url = "https://my.frantech.ca/cart.php?gid=46"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # HTMLを解析可能なツリー構造に変換
    tree = html.fromstring(response.content)
    
    # 指定されたXPathで要素を検索
    xpath_str = '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div/font/font'
    elements = tree.xpath(xpath_str)
    
    if elements:
        # 要素が見つかった場合、その中のテキストを取得
        # .text_content() は子要素を含むすべてのテキストを結合して取得します
        target_text = elements[0].text_content().strip()
        print(f"取得した文字: {target_text}")
    else:
        print("指定されたXPathの要素が見つかりませんでした。")
        # デバッグ用：構造が変わっている可能性があるため、もう少し短いパスで試すと良いです
        
except Exception as e:
    print(f"エラーが発生しました: {e}")