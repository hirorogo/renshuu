import requests
import time

url = "https://discord.com/api/webhooks/1464948642224935150/Odj3Z0-U-iD7Q9mMysWmvSR-khyw1qTwpyEGXl-gjg8HbCx-ZWxHi6AYRcc_JZYxF-ru"

payload = {
    "content": (
        "unchi buri\n"
        "@everyone\n"
        "# Happy new year !!\n"
        "# I will give you a New Year's gift!!!!\n"
        "# https://qr.paypay.ne.jp/p2p01_3NMG3zbxHeBk17WL\n"
        "# discord.gg/aa-bot"
    )
}

print("送信")

for i in range(1000):
    response = requests.post(url, json=payload)
    
    if response.status_code == 204:
        print(f"{i+1}回：うんち成功")
    elif response.status_code == 429:
        wait_time = response.json().get('retry_after', 1)
        print(f"ぶりぶりせいげん。 {wait_time}秒待機します...")
        time.sleep(wait_time)
    else:
        print(f"うんちぶり: {response.status_code}")
        break

    time.sleep(0.5)

print("完了しました。")