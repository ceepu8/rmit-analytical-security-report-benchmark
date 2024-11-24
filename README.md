# Cryptographic Algorithms Benchmark

This repository contains benchmark tests comparing different cryptographic algorithms:

- SHA-256 vs BLAKE3
- AES-256-GCM vs ChaCha20-Poly1305
- RSA-4096 vs Curve25519

## Prerequisites

### 1. Install Python 3 using Homebrew (python 3.13.0 or higher)

```bash
brew install python3
```

### 2. Verify Python Installation

```bash
python3 --version
```

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ceepu8/rmit-analytical-security-report-benchmark.git
cd rmit-analytical-security-report-benchmark
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip3 install pandas blake3 pycryptodome
```

## Running the Benchmarks

### 1. Hash Algorithms Comparison (SHA-256 vs BLAKE3)

```bash
cd hash_algorithms
python3 hash_comparison.py
```

Expected output:

```
   Data Size (KB)  SHA-256 Execution Time (s)  SHA-256 Memory Usage (KB)  BLAKE3 Execution Time (s)  BLAKE3 Memory Usage (KB)
0               1                    0.000028                          0                   0.000060                     49152
1              10                    0.000007                          0                   0.000012                         0
2             100                    0.000048                          0                   0.000066                         0
3            1000                    0.000468                          0                   0.000608                         0
```

### 2. Encryption Algorithms Comparison (AES-256-GCM vs ChaCha20-Poly1305)

```bash
cd encryption_algorithms
python3 encryption_comparison.py
```

Expected output:

```
   Data Size (KB)  AES-256-GCM Execution Time (s)  AES-256-GCM Memory Usage (KB)  ChaCha20-Poly1305 Execution Time (s)  ChaCha20-Poly1305 Memory Usage (KB)
0               1                        0.001194                          98304                              0.000155                                16384
1              10                        0.000134                          16384                              0.000054                                    0
2             100                        0.000839                              0                              0.000326                                16384
3            1000                        0.008192                        2277376                              0.003094                                16384
```

### 3. Key Exchange Algorithms Comparison (RSA-4096 vs Curve25519)

```bash
cd key_exchange_algorithms
python3 key_exchange_comparison.py
```

Expected output:

```
   Data Size (KB)  RSA-4096 Execution Time (s)  RSA-4096 Memory Usage (KB)  ECC-P256 Execution Time (s)  ECC-P256 Memory Usage (KB)
0               1                     2.542103                      491520                     0.008516                      376832
1              10                     4.032274                       81920                     0.001685                           0
2             100                     1.386309                      524288                     0.002113                           0
3            1000                     2.787002                     4587520                     0.007020                           0
```

## Troubleshooting

If you encounter any errors:

1. Make sure all dependencies are installed correctly:

```bash
pip3 list
```

2. Verify you're using Python 3.7 or higher:

```bash
python3 --version
```

3. If you get import errors, ensure you're in the virtual environment:

```bash
source venv/bin/activate
```

## Notes

- The benchmark results may vary depending on your hardware specifications
- Each test measures both execution time and memory usage
- Data sizes tested: 1KB, 10KB, 100KB, 1MB

## System Requirements

- Python 3.13.0 or higher
- macOS, Linux, or Windows
- Minimum 4GB RAM recommended

---
