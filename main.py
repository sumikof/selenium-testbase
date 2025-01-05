from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import os

from driver_factory import EdgeDriver, create_driver


# 保存先ディレクトリ
output_directory = r"C:\temp"
os.makedirs(output_directory, exist_ok=True)  # ディレクトリが存在しない場合は作成


# WebDriverのサービスを作成
driver = create_driver(EdgeDriver)

try:
    # 指定のURLを開く
    driver.get("https://www.yahoo.co.jp/")
    print("Yahooのページを開きました")

    # ページタイトルを取得して確認
    print(f"ページタイトル: {driver.title}")

    # 画面キャプチャを取得して保存
    # screenshot_path = os.path.join(output_directory, "screenshot.png")
    # driver.save_screenshot(screenshot_path) 
    # print(f"画面キャプチャを取得して {screenshot_path} に保存しました")
    
    screenshot_path = os.path.join(output_directory, "screenshot_full_headless2.png")
    driver.full_screenshot(screenshot_path)
    print(f"DevToolsプロトコルを使用したページ全体のスクリーンショットを保存しました: {screenshot_path}")


finally:
    # ブラウザを閉じる
    driver.quit()
    print("Edgeブラウザを閉じました")
