import os
import logging

import pytest

from src.driver_factory import EdgeDriver, create_driver

logger = logging.getLogger("test_logger")


@pytest.fixture
def test_web_driver():
    web_driver = create_driver(EdgeDriver)
    yield web_driver
    web_driver.quit()
    logging.info("Edgeブラウザを閉じました")


def test_edge_screenshot(test_web_driver, tmp_path):
    # 指定のURLを開く
    test_web_driver.get("https://www.yahoo.co.jp/")
    logging.info("Yahooのページを開きました")

    # ページタイトルを取得して確認
    logging.info(f"ページタイトル: {test_web_driver.title}")

    # 画面キャプチャを取得して保存
    screenshot_path = os.path.join(tmp_path, "screenshot_full_headless.png")
    test_web_driver.full_screenshot(screenshot_path)
