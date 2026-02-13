import json
import os
from urllib.parse import urlparse
from collections import defaultdict

# --- 設定エリア (macOS用) ---
# Chromeの場合のパス
BOOKMARK_PATH = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Bookmarks')
# Braveなど他のブラウザを使っている場合はここを調整
# BOOKMARK_PATH = os.path.expanduser('~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Bookmarks')
# Braveの場合のパス

BOOKMARK_PATH = os.path.expanduser('~/Library/Application Support/BraveSoftware/Brave-Browser/Default/Bookmarks')

OUTPUT_FILE = 'domain_sorted_bookmarks.txt'

def extract_bookmarks(nodes, found_links):
    for node in nodes:
        if node.get('type') == 'url':
            found_links.append({'name': node['name'], 'url': node['url']})
        elif node.get('type') == 'folder':
            extract_bookmarks(node.get('children', []), found_links)

def sort_by_domain():
    if not os.path.exists(BOOKMARK_PATH):
        print(f"エラー: ブックマークファイルが見つかりません。\nパスを確認してください: {BOOKMARK_PATH}")
        return

    with open(BOOKMARK_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    all_links = []
    for root_key in data['roots']:
        extract_bookmarks([data['roots'][root_key]], all_links)

    # ドメインごとにグループ化
    domain_map = defaultdict(list)
    for link in all_links:
        domain = urlparse(link['url']).netloc
        if domain:
            domain_map[domain].append(link)

    # 件数が多い順にソート
    sorted_domains = sorted(domain_map.items(), key=lambda x: len(x[1]), reverse=True)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"合計ブックマーク数: {len(all_links)}\n")
        f.write("=" * 40 + "\n\n")

        for domain, links in sorted_domains:
            f.write(f"【 {domain} 】 ({len(links)}件)\n")
            for link in links:
                f.write(f"  - {link['name']}\n    {link['url']}\n")
            f.write("\n" + "-"*20 + "\n\n")

    print(f"整理が完了しました！\n出力先: {os.path.abspath(OUTPUT_FILE)}")
    print(f"ドメイン数: {len(sorted_domains)}")

if __name__ == "__main__":
    sort_by_domain()