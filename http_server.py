class HTTPServer:
    
    def handle_request(self, data):
        response_line = b'HTTP/1.1 200 OK\r\n'
        blank = b'\r\n'
        response_body = b"<p>Hello World!</p>"

        return b''.join([response_line, blank, response_body])
    

