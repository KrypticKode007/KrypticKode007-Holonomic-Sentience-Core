from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class PrometheusMetricsAPI:
    def __init__(self, state, port=8080):
        self.state = state
        self.port = port
        self.server = None

    def start(self):
        state_ref = self.state
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/metrics":
                    self.send_response(200)
                    self.end_headers()
                    metrics = f"kryptic_hope_level {state_ref.hope_level}\nkryptic_exhaustion {state_ref.exhaustion}\n"
                    self.wfile.write(metrics.encode('utf-8'))
            def log_message(self, format, *args): return

        try:
            self.server = HTTPServer(("127.0.0.1", self.port), Handler)
            self.server.serve_forever()
        except Exception: pass

    def stop(self):
        if self.server:
            self.server.shutdown()
          
