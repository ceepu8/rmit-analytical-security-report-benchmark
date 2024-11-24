import time
import resource
import os
from Crypto.Cipher import AES, ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
import pandas as pd

def measure_performance(algorithm, data):
    start_time = time.time()
    memory_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    key = get_random_bytes(32)  # 256-bit key
    
    if algorithm == 'aes256-gcm':
        cipher = AES.new(key, AES.MODE_GCM)
        cipher.update(b"header")
        ciphertext, tag = cipher.encrypt_and_digest(data)
    
    elif algorithm == 'chacha20-poly1305':
        cipher = ChaCha20_Poly1305.new(key=key)
        cipher.update(b"header")
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
    end_time = time.time()
    memory_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = memory_after - memory_before
    
    return execution_time, memory_usage

data_sizes = [1024, 10240, 102400, 1024000]
results = []

for size in data_sizes:
    data = b"random_data" * (size // 10)
    
    aes_time, aes_memory = measure_performance('aes256-gcm', data)
    chacha_time, chacha_memory = measure_performance('chacha20-poly1305', data)
    
    results.append({
        "Data Size (KB)": size // 1024,
        "AES-256-GCM Execution Time (s)": aes_time,
        "AES-256-GCM Memory Usage (KB)": aes_memory,
        "ChaCha20-Poly1305 Execution Time (s)": chacha_time,
        "ChaCha20-Poly1305 Memory Usage (KB)": chacha_memory
    })

df = pd.DataFrame(results)
print(df)