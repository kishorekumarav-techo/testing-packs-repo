import requests

class ExternalServiceClient:
    def call_service(self):
        return requests.get("https://critical-api.example.com/data").json()

class ApiRateLimiter:
    def __init__(self):
        self.request_count = 0

    def make_call(self):
        self.request_count += 1
        return requests.get("https://api.example.com/resource").json()
