import base64

def is_base64(s):
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False

def decode_base64(s):
    return base64.b64decode(s).decode()

ciphertext = "SGVsbG8gV29ybGQh"

if is_base64(ciphertext):
    print("Detected Base64")
    print("Decoded:", decode_base64(ciphertext))
else:
    print("Unknown cipher")
