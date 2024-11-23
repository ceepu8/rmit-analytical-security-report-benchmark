# Python Code Example for Benchmarking.
## **Guide to running Python code on MacBook Pro M1 and getting parameters for reports**

### **Step 1: Install Python and necessary libraries**
Before starting, you need to make sure that you have Python 3.13.0 installed on your MacBook Pro M1.

1. **Install Python 3.13.0** (if not already installed):
- You can download and install the latest version of Python from the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/).
- After installation, you can check by opening **Terminal** and typing:
```bash
python3 --version
```
This will display the current version of Python, make sure you are using Python 3.13.0.

2. **Install Required Libraries:**
- Although the code doesn't require installing additional libraries beyond standard Python, you can still make sure that libraries like **random**, **string**, **time**, and **resource** are available in your Python environment.

### **Step 2: Run the Python Code**

1. **Create a Python File**:
- Open a **Text Editor** or **IDE** (like **Visual Studio Code**, **PyCharm**, or **Sublime Text**) and create a new file called **benchmark.py**.
- Paste the provided Python code into this file.

2. **Run the Python Code in Terminal**:
- Open **Terminal** on your Mac.
- Navigate to the directory containing the **benchmark.py** file (for example, if your file is in the **RMIT/code-test** folder, type the following command in Terminal):
```bash
cd ~/code-test
```
- Run the Python file using the command:
```bash
python3 benchmark.py
```

### **Step 3: Get the result parameters**
After running the code, you will get results similar to the following in Terminal:

```
Data Size: 1KB | Execution Time: 0.00012 seconds | Memory Usage: 0.52 KB
Data Size: 10KB | Execution Time: 0.00122 seconds | Memory Usage: 5.24 KB
Data Size: 100KB | Execution Time: 0.01234 seconds | Memory Usage: 52.68 KB
Data Size: 1000KB | Execution Time: 0.12345 seconds | Memory Usage: 524.78 KB
```

- **Execution Time**: The time it takes for the program to process data. This parameter is measured in seconds.
- **Memory Usage**: The amount of memory the program uses during execution, measured in kilobytes (KB).
