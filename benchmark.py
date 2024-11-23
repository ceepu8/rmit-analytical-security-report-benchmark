import time
import resource
import hashlib
import blake3

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
data_1kb = b"random_data" * 128  # 1KB
data_1mb = b"random_data" * 1024 * 1024  # 1MB

# Measure performance for both algorithms
sha256_time_1kb, sha256_memory_1kb = measure_performance('sha256', data_1kb)
blake3_time_1kb, blake3_memory_1kb = measure_performance('blake3', data_1kb)

# Output the results
print(f"SHA-256 - 1KB: Time = {sha256_time_1kb:.6f}s, Memory = {sha256_memory_1kb}KB")
print(f"BLAKE3 - 1KB: Time = {blake3_time_1kb:.6f}s, Memory = {blake3_memory_1kb}KB")

# Run for larger data
sha256_time_1mb, sha256_memory_1mb = measure_performance('sha256', data_1mb)
blake3_time_1mb, blake3_memory_1mb = measure_performance('blake3', data_1mb)

print(f"SHA-256 - 1MB: Time = {sha256_time_1mb:.6f}s, Memory = {sha256_memory_1mb}KB")
print(f"BLAKE3 - 1MB: Time = {blake3_time_1mb:.6f}s, Memory = {blake3_memory_1mb}KB")
