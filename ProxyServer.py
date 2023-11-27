import socket
import re

# Server configuration
host = 'localhost'
port = 8083  # Port on which the server will listen
max_connections = 5  # Maximum number of connections the server will accept

# List of blocked sites for content filtering
block_list = ['facebook', 'linkedin']

# Cache to store previously fetched URLs
cache = {}

def start_server(host, port):
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server.bind((host, port))

    # Listen for incoming connections
    server.listen(max_connections)
    print(f"Server listening on port {port}...\n")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")

        # Receive URL from the client
        url = client_socket.recv(1024).decode()
        print(f"Received URL: {url}")

        # Check if the site is blocked
        blocked = False
        for site in block_list:
            if re.search(site, url):
                print("This site is blocked")
                blocked = True
                break

        if blocked:
            response = "blocked"
        else:
            # Check if the URL is in the cache
            if url in cache:
                print("Fetching from cache...")
                response = cache[url]
                cache_or_web = "URL cached from cache"
                print("URL cached from cache")
            else:
                # Fetch the URL from the web server
                response = url
                print("URL fetched from web server")
                cache_or_web = "URL fetched from web server"
                # Add URL to the cache
                cache[url] = response

        # Send the response back to the client
        client_socket.send(response.encode())
        client_socket.send(cache_or_web.encode())

        # Close the socket connection
        client_socket.close()

if __name__ == '__main__':
    start_server(host, port)
