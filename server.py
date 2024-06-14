from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("Received POST data: %s", post_data.decode('utf-8'))
        print("Received POST data:", post_data.decode('utf-8'))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting test server...')
    print('Starting test server...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
