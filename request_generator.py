import base64
import hmac
import json
import hashlib

API_HASHING_KEY = b"22CSMTOOL2022"
def body_generator(object):
    json_str = json.dumps(object)
    json_bytes = json_str.encode('utf-8')
    base64_bytes = base64.b64encode(json_bytes)
    encoded_payload= base64_bytes.decode('utf-8')
    hmac_token = hmac.new(API_HASHING_KEY, encoded_payload.encode('utf-8'), hashlib.sha256).hexdigest()
    body = {    
        "REQUEST_DATA": encoded_payload,
        "REQUEST_TOKEN": hmac_token
    }
    return body