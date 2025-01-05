import base64
import logging

from selenium import webdriver
from selenium.webdriver.edge.service import Service

logger = logging.getLogger("test_logger")

class Driver:
    pass

# Edge WebDriverのパスを指定
edge_driver_path = r"C:\app\edgedriver\msedgedriver.exe"  # msedgedriverのパスを指定
edge_executable_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Edgeの実行ファイルパス
iedriver_executable_path = r"C:\app\edgedriver\IEDriverServer.exe"  # IEDriverServer


class EdgeDriver(webdriver.Edge):
    def __init__(self):
        # WebDriverのオプションを設定
        options = webdriver.EdgeOptions()
        options.add_argument('--headless') # ヘッドレスモードで起動
        service = Service(edge_driver_path)
        super().__init__(service=service, options=options)
        # options.add_argument("--disable-gpu")
        # options.add_argument("window-size=1920,1080")
        options.add_argument("--inprivate")  # プライベートモードで起動
        options.add_argument("ie-mode-file=https://www.yahoo.co.jp/")  # IEモードで開くURLを指定
        options.add_experimental_option("ieMode", True)  # IEモードを有効化

    def full_screenshot(self, file_path):
        width = self.execute_script("return document.body.scrollWidth;")
        height = self.execute_script("return document.body.scrollHeight;")
        viewport = {
            "x": 0, 
            "y": 0,
            "width": width,
            "height": height,
            "scale": 1
        }
        # Chrome Devtools Protocolコマンドを実行し、取得できるBase64形式の画像データをデコードしてファイルに保存
        image_base64 = self.execute_cdp_cmd("Page.captureScreenshot", {"clip": viewport, "captureBeyondViewport": True})
        image = base64.b64decode(image_base64["data"])
        with open(file_path, 'bw') as f:
            f.write(image)
        logger.info(f"DevToolsプロトコルを使用したページ全体のスクリーンショットを保存しました: {file_path}")


class IEDriver(webdriver.Ie):
    def __init__(self):
        # IEモード用のWebDriverサービスを作成
        service = Service(iedriver_executable_path)

        # IEオプションの設定
        options = webdriver.IeOptions()
        options.attach_to_edge_chrome = True  # Edge IEモードを有効化
        options.edge_executable_path = edge_executable_path

        # WebDriverの起動
        super().__init__(service=service, options=options)

    def full_screenshot(self, file_path):
        # 画面キャプチャを取得して保存
        self.save_screenshot(file_path) 
        logger.info(f"画面キャプチャを取得して {file_path} に保存しました")

def create_driver(driver_type):
    return driver_type()
