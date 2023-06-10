import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Environment:
    def __init__(self):
        self.app_env = os.environ.get("FLASK_ENV") or "development"
        self.base_url = os.environ.get("BASE_URL")

        # Adyen Credentials
        self.adyen_xapi_key = os.environ.get("ADYEN_XAPI_KEY")
        self.adyen_platform = os.environ.get("ADYEN_PLATFORM") or "test"
        self.adyen_merchant_acct = os.environ.get("ADYEN_MERCHANT_ACCT")


config = Environment()
