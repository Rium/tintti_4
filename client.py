import socket

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The same port as used by the server

def send_request(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        return response

# Example usage: send an ECHO request
request = "ECHO Hello, this is a test message."
response = send_request(request)
print(f"Server response: {response}")
# Example for the GET request
request = "GET testfile.txt"
response = send_request(request)
if response: print(f"Contents of the file:\n{response}")
# Example for the STATS request
request = "STATS"
print(send_request(request))

# Example for the 2nd question
request = "GET security_test/passwd.txt"
response = send_request(request)
if response: print(response)
# Examples for the 3rd question
request = "TEST"
response = send_request(request)
print(response)
request = "TEST test"
response = send_request(request)
print(response) 
