from django.conf import settings
import requests

class PayStack:
    PAYSTACK_SECRET_KEY = 'sk_test_212aef506c8d43e3c4877ef5369800950d18d0b6'
    base_url = "https://api.paystack.co"

    def verify_payment(self ,ref ,*args,**kwargs):
        path = f"/transaction/verify/:{ref}"

        header = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "content-type": "application/json",
        }
        url = self.base_url + path
        response = requests.get(url,headers=header)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data["data"]
        response_data = response.json()
        return response_data["status"], response_data["message"]
