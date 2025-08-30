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