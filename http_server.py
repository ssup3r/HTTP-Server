class HTTPServer:

    headers = {
        'Server': 'SuperHTTPServer/1.0',
        'Content-Type': 'text/html'
        
    }
    status_codes = {
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        103: "Early Hints",
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        207: "Multi-Status",
        208: "Already Reported",
        226: "IM Used",
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        417: "Expectation Failed",
        418: "I'm a teapot",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        425: "Too Early",
        426: "Upgrade Required",
        428: "Precondition Required",
        429: "Too Many Requests",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        509: "Bandwidth Limit Exceeded",
        510: "Not Extended",
        511: "Network Authentication Required",
        598: "Network Read Timeout Error",
        599: "Network Connect Timeout Error"
    }

    def handle_request(self, data):

        response_line = self.response_line(status_code=200)
        response_header = self.response_headers()
        blank = b'\r\n'
        response_body = b"<p>Hello World!</p>"

        return b''.join([response_line, blank, response_header, blank, response_body])
    def response_line(self, status_code):
        return (f"HTTP/1.1 {status_code} {self.status_codes[status_code]}").encode()
    def response_headers(self, extra_headers=None):
        headers = self.headers.copy()
        if extra_headers:
            headers.update(extra_headers)
        response_header = ""
        for j in headers:
            response_header += f"{j}: {headers[j]}\r\n"
        return response_header.encode()

