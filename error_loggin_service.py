import logging
import requests

logging.basicConfig(level=logging.INFO)

def risky_network_call():
    resp = requests.get("https://external-service.example.com/data")
    return resp.json()

def fail_gracefully_example():
    try:
        risky_network_call()
    except Exception:
        logging.error("Something went wrong.")
