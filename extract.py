import http.client
import json
from dotenv import load_dotenv
import os


load_dotenv()

def extract_data():
    conn = os.getenv("url")

    headers = os.getenv("api_key")
    
    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    gasprices_data = json.loads(data)
    return gasprices_data