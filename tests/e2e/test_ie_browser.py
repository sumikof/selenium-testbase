import os
import logging

from src.driver_factory import IEDriver, create_driver

logger = logging.getLogger("test_logger")


def test_ie_screenshot(tmp_path):
    driver = create_driver(IEDriver)
    try:
        # 指定のURLを開く
        driver.get("https://www.wikipedia.org/")
        logging.info("wikipediaのページを開きました")

        # ページタイトルを取得して確認
        logging.info(f"ページタイトル: {driver.title}")

        # 画面キャプチャを取得して保存
        screenshot_path = os.path.join(tmp_path, "screenshot_full_headless.png")
        driver.full_screenshot(screenshot_path)
    finally:
        # ブラウザを閉じる
        driver.quit()
        logging.info("IEブラウザを閉じました")
