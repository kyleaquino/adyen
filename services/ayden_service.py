import uuid
from Adyen import Adyen
from server.environment import config


class AdyenCheckout:
    def __init__(self, data: dict = None):
        self.adyen = Adyen(
            xapikey=config.adyen_xapi_key,
            platform=config.adyen_platform,
            merchant_account=config.adyen_merchant_acct,
        )

        data = data or {}
        amount = data.get("amount") or {}
        self.base_amount = amount.get("value")
        self.base_currency = amount.get("currency") or "USD"

        self.reference = data.get("reference") or str(uuid.uuid4())
        self.return_url = data.get("returnUrl")
        self.merchant_account = data.get("merchantAccount") or config.adyen_merchant_acct
        self.shopper_reference = data.get("shopperReference")
        self.country_code = data.get("countryCode") or "US"
        self.shopper_email = data.get("shopperEmail")
        self.shopper_locale = data.get("shopperLocale") or "en-US"

        # Result Parameters
        self.payment_id = data.get("id")
        self.reusable = data.get("reusable")
        self.expires_at = data.get("expiresAt")
        self.url = data.get("url")
        self.status = data.get("status")

    def to_json(self):
        """
        Parse AdyenCheckout line items to json
        """
        return {
            "amount": {"currency": self.base_currency, "value": self.base_amount},
            "reference": self.reference,
            "returnUrl": self.return_url,
            "merchantAccount": self.merchant_account,
            "shopperReference": self.shopper_reference,
            "countryCode": self.country_code,
            "shopperEmail": self.shopper_email,
            "shopperLocale": self.shopper_locale,
        }

    def payment_links(self, request):
        return AdyenCheckout(self.adyen.checkout.payment_links_api.payment_links(request).message)

    def create_payment(self, amount, currency, return_url):
        self.base_amount = amount
        self.base_currency = currency
        self.return_url = return_url

        return self.payment_links(self.to_json())
