import time
import resource
from Crypto.PublicKey import RSA
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import pandas as pd

def measure_performance(algorithm, data):
    start_time = time.time()
    memory_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    data_encrypted = None
    if algorithm == 'rsa-4096':
        # Generate RSA 4096-bit key pair
        rsa_key = RSA.generate(4096)
        rsa_cipher = PKCS1_OAEP.new(rsa_key.publickey())

        # Generate a random AES key
        aes_key = get_random_bytes(32)  # AES-256

        # Encrypt the AES key using RSA
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        # Encrypt the data using AES
        aes_cipher = AES.new(aes_key, AES.MODE_GCM)
        nonce = aes_cipher.nonce
        ciphertext, tag = aes_cipher.encrypt_and_digest(data)

        # Combine the encryption results
        data_encrypted = (encrypted_aes_key, nonce, tag, ciphertext)
        
        # Decrypt the data to verify the process
        rsa_decipher = PKCS1_OAEP.new(rsa_key)
        decrypted_aes_key = rsa_decipher.decrypt(encrypted_aes_key)
        
        aes_decipher = AES.new(decrypted_aes_key, AES.MODE_GCM, nonce=nonce)
        decrypted_data = aes_decipher.decrypt_and_verify(ciphertext, tag)
        
        assert data == decrypted_data, "Decrypted data does not match original data"
        
    elif algorithm == 'ecc-p256':
        # Generate ECC key pair on P-256 curve
        ecc_key = ECC.generate(curve='P-256')
        h = SHA256.new(data)
        signer = DSS.new(ecc_key, 'fips-186-3')
        signature = signer.sign(h)
        
        # Verify the signature to complete the process
        verifier = DSS.new(ecc_key.public_key(), 'fips-186-3')
        try:
            verifier.verify(h, signature)
        except ValueError:
            raise ValueError("The signature is not valid.")
        
    end_time = time.time()
    memory_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = memory_after - memory_before
    
    return execution_time, memory_usage

data_sizes = [1024, 10240, 102400, 1024000]
results = []

for size in data_sizes:
    # Generating random data of required size
    data = b"random_data" * (size // 10)
    
    rsa_time, rsa_memory = measure_performance('rsa-4096', data)
    ecc_time, ecc_memory = measure_performance('ecc-p256', data)
    
    results.append({
        "Data Size (KB)": size // 1024,
        "RSA-4096 Execution Time (s)": rsa_time,
        "RSA-4096 Memory Usage (KB)": rsa_memory,
        "ECC-P256 Execution Time (s)": ecc_time,
        "ECC-P256 Memory Usage (KB)": ecc_memory
    })

# Creating a DataFrame to show results
df = pd.DataFrame(results)
print(df)