# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
## Developed by : SANJAY KUMAR B
## REG NO       :212224230242
```
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<head>
</title>
</head>
<body bgcolor="yellow">
<table border="1" align="center" bgcolor="cyan" cellpadding="10">
<caption><h1>List of Protocols</h1></caption>
<tr><th>S.No.</th><th>Name of the Layers</th>
<th>Name of the Protocols</th></tr><tr>
<td>1</td><td>Application Layer</td><td>HTTP, FTP</td></tr><tr>
<td>2</td><td>Transport Layer</td><td>TCP & UDP</td></tr><tr></tr>
<td>3<td>network layer</td><td>ip,arp</td><tr></tr>
<td>3<td>phy layer</td><td>mac,ethernet</td><tr></tr>
</tr></table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
``` 

## OUTPUT:
<img width="1920" height="1200" alt="Screenshot 2025-08-30 093020" src="https://github.com/user-attachments/assets/4e624f7e-3dc1-410f-a70d-e4d0cc7a18f0" />

## RESULT:
The program for implementing simple webserver is executed successfully.
