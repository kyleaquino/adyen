from services.ayden_service import AdyenCheckout

checkout = AdyenCheckout()
result = checkout.create_payment(1000, "USD", "test.org")

print(result)
