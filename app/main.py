import os
import http.server
import socketserver

PORT = 8080

class StudentHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        
        name = os.getenv("STUDENT_NAME", "Timur")
        surname = os.getenv("STUDENT_SURNAME", "Baigashev")
        group = os.getenv("STUDENT_GROUP", "IT2-2312")
        student_id = os.getenv("STUDENT_ID", "37540")
        
        body = (
            "================================\n"
            "DevOps Student Application\n"
            "================================\n"
            f"Name: {name}\n"
            f"Surname: {surname}\n"
            f"Group: {group}\n"
            f"Student ID: {student_id}\n"
            "Application is running successfully!\n"
        )
        self.wfile.write(body.encode("utf-8"))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), StudentHandler) as httpd:
        httpd.serve_forever()
