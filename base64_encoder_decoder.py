import base64

def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(f"Encoded password: {encoded_bytes.decode()}")

user_pass = input("Enter your password: ")
encrypt_pass(user_pass)

def decrypt_pass(password):
    decoded_bytes = base64.b64decode(password.encode())
    decoded_data = decoded_bytes.decode()
    print(f"Decoded password: {decoded_data}")

encoded_string = input("Enter the Base64 string: ")
decrypt_pass(encoded_string)