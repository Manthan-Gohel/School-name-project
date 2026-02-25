import sys
try:
    with open('server_log.txt', 'rb') as f:
        data = f.read()
    try:
        print(data.decode('utf-16le'))
    except:
        print(data.decode('utf-8', errors='ignore'))
except Exception as e:
    print(f"Error: {e}")
