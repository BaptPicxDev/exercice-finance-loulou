import pandas as pd
import yfinance as yf


def retrieve_hist_assets(assets: list) -> list:
    """Retrieve asset history values.

    N.B.:
        - package link: https://pypi.org/project/yfinance/
    :param assets: list of assets (max 5)
    :return: asset historical list
    """
    for asset in assets:
        msft = yf.Ticker(asset)
        print(dir(msft))
        print(msft.get_info())
        hist = msft.history(period="1mo")


if __name__ == "__main__":
    print("Hello")
    retrieve_hist_assets(["APPL", "null"])
