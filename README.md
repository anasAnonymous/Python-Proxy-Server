# Python Proxy Server

## Overview

This is a simple proxy server implemented in Python with a focus on content filtering and caching. The proxy acts as an intermediary between a client and a web server, providing basic content filtering to block access to specific websites and caching previously fetched URLs for improved performance.

## Features

- **Content Filtering:** Block access to specified websites based on a predefined block list.
- **Caching:** Store and retrieve previously fetched URLs to reduce load times.
- **Web Browser Interaction:** Open allowed URLs in the default web browser.
- **Simple and Lightweight:** Designed for simplicity with Python as the primary implementation language.

## Libraries Used

- **Socket:** Used for creating the server-client communication.
- **JSON:** Utilized for encoding and decoding JSON data.
- **Webbrowser:** Enables opening URLs in the default web browser.
- **Cryptography:** Implements message signing for enhanced security.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/anasAnonymous/python-proxy-server.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd python-proxy-server
   ```

3. **Install Dependencies:**
   ```bash
   pip install cryptography
   ```

4. **Customize Block List:**
   - Open `proxy_server.py` and customize the `block_list` variable with websites you want to block.

5. **Run the Server:**
   ```bash
   python proxy_server.py
   ```

6. **Run the Client:**
   ```bash
   python proxy_client.py
   ```
   
7. **Enter the URL when prompted on the client side.**


## Requirements
- Python 3.x
- Cryptography library


## Contributions
Contributions are welcome! Feel free to open issues, submit pull requests, or provide suggestions for improvement.


