from web3.auto import w3
import binascii

# Replace these variables with your actual keystore file path and password
password = ""
filename = "/Users/krishsahoo/PycharmProjects/EthereumP/ethprivate/keystore/UTC--2024-03-01T01-46-11.653602000Z--0eba61c1a594a79db55bc787a41588e026ac1d49"

# This function will read the keystore file and decrypt the private key
def extract_private_key(password, filename):
    with open(filename) as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key, password)
        return binascii.b2a_hex(private_key).decode('ascii')

# Extract the private key
private_key_hex = extract_private_key(password, filename)
print(f"Your private key is: {private_key_hex}")

# Save this private key or use it as needed for your dApp development
# 363c50fb89e0fb016cdf095b7d3d66e31ad0eab34dbba866a5b7d486f5e1d877

#Sent hash "0xd46c66f8d340fb4a8099f717d0ed2c4537bb5970879982adc2a25a78accd82a2"
