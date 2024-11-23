import time
import resource
import hashlib
import blake3
import pandas as pd

# Function to measure execution time and memory usage
def measure_performance(algorithm, data):
    start_time = time.time()
    memory_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    # Run the algorithm
    if algorithm == 'sha256':
        hash_object = hashlib.sha256(data)
    elif algorithm == 'blake3':
        hash_object = blake3.blake3(data)
    
    hash_object.hexdigest()  # Force computation to get the result
    
    end_time = time.time()
    memory_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    execution_time = end_time - start_time
    memory_usage = memory_after - memory_before  # in KB
    
    return execution_time, memory_usage

# Generate random data of varying sizes
data_sizes = [1024, 10240, 102400, 1024000]  # 1KB, 10KB, 100KB, 1000KB
results = []

for size in data_sizes:
    data = b"random_data" * (size // 10)  # Create data based on the size
    
    sha256_time, sha256_memory = measure_performance('sha256', data)
    blake3_time, blake3_memory = measure_performance('blake3', data)
    
    # Append the results to the list
    results.append({
        "Data Size (KB)": size // 1024,
        "SHA-256 Execution Time (s)": sha256_time,
        "SHA-256 Memory Usage (KB)": sha256_memory,
        "BLAKE3 Execution Time (s)": blake3_time,
        "BLAKE3 Memory Usage (KB)": blake3_memory
    })

# Convert results to DataFrame for better visualization
df = pd.DataFrame(results)

# Display the results
print(df)
