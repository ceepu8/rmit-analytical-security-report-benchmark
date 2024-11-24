import time
import resource
import hashlib
import blake3
import pandas as pd

def measure_performance(algorithm, data):
    start_time = time.time()
    memory_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    if algorithm == 'sha256':
        hash_object = hashlib.sha256(data)
    elif algorithm == 'blake3':
        hash_object = blake3.blake3(data)
    
    hash_object.hexdigest()
    
    end_time = time.time()
    memory_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = memory_after - memory_before
    
    return execution_time, memory_usage

data_sizes = [1024, 10240, 102400, 1024000]
results = []

for size in data_sizes:
    data = b"random_data" * (size // 10)
    
    sha256_time, sha256_memory = measure_performance('sha256', data)
    blake3_time, blake3_memory = measure_performance('blake3', data)
    
    results.append({
        "Data Size (KB)": size // 1024,
        "SHA-256 Execution Time (s)": sha256_time,
        "SHA-256 Memory Usage (KB)": sha256_memory,
        "BLAKE3 Execution Time (s)": blake3_time,
        "BLAKE3 Memory Usage (KB)": blake3_memory
    })

df = pd.DataFrame(results)
print(df)
