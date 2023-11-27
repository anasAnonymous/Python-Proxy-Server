import socket
import webbrowser

# Define the server address and maximum number of requests
server_address = ('localhost', 8083)
max_request = 5

# Cache to store previously fetched URLs
cache = {}

# Loop for multiple requests
for i in range(max_request):
    # Get user input for the URL
    url = input(f"Enter URL {i + 1}: ")

    try:
        # Create a socket and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)

        # Send the URL to the server
        client_socket.send(url.encode())

        # Receive response from the server
        response = client_socket.recv(1024).decode()
        cache_or_web = client_socket.recv(1024).decode()

        # Check if the URL is blocked
        if response == "blocked":
            print("Blocked")
            cache[url] = "blocked"
        else:
            # Open the URL in the browser
            print("Not blocked")
            webbrowser.open(response)
            cache[url] = response
            print(cache_or_web)

        # Close the socket
        client_socket.close()

    except Exception as e:
        print(f"Error occurred: {e}")
