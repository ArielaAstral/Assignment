import base64
import json
import requests
def result_generator(url,data):
    response = requests.post(url, json=data)
    temp = response.json()
    encoded_data = temp['RESPONSE_DATA']
    decoded_bytes = base64.b64decode(encoded_data)
    decoded_json = json.loads(decoded_bytes)
    return decoded_json