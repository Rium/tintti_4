import socket
import os

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432  # Port number (you can change this)
stats = [["ECHO", 0], ["GET", 0], ["STATS", 0]] # Keeping track of how many times different methods have been called

def handle_request(request):
    # Split the request line into method and parameter, unless the request is for stats in which case there is only the method
    parts = request.strip().split(' ', 1)
    if len(parts) < 2 and request != "STATS":
        return "ERROR: Invalid request format"

    # If the request is for stats only the method is needed
    if len(parts) == 1: method = parts[0]
    else: method, parameter = parts[0], parts[1]
    
    # Handle the "ECHO" method
    if method == "ECHO":
        stats[0][1] += 1
        return parameter
    # Handle the "GET" method
    elif method == "GET":
        stats[1][1] += 1
        file = os.path.join("./", parameter)

        if os.path.isfile(file):
            with open(file, "r") as request_file:
                content = request_file.read()
                return content
            
            return file
        return "ERROR: File not found"
    # Handle the "STATS" method
    elif method == "STATS":
        stats[2][1] += 1
        return_stats = ""
        for i in stats:
            return_stats += f"{i[0]}: {i[1]}\n"
        return return_stats.strip()
    else:
        return "ERROR: Unknown method"

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is running on {HOST}:{PORT}...")
        
        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                response = handle_request(data)
                client_socket.sendall(response.encode('utf-8'))


run_server()
