import os
import logging

import pytest

from src.driver_factory import EdgeDriver, create_driver

logger = logging.getLogger("test_logger")


@pytest.fixture
def driver():
    return create_driver(EdgeDriver)


def test_edge_screenshot(driver, tmp_path):
    try:
        # 指定のURLを開く
        driver.get("https://www.yahoo.co.jp/")
        logging.info("Yahooのページを開きました")

        # ページタイトルを取得して確認
        logging.info(f"ページタイトル: {driver.title}")

        # 画面キャプチャを取得して保存
        screenshot_path = os.path.join(tmp_path, "screenshot_full_headless.png")
        driver.full_screenshot(screenshot_path)
    finally:
        # ブラウザを閉じる
        driver.quit()
        logging.info("Edgeブラウザを閉じました")
