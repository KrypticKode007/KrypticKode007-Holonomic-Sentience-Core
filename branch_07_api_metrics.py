#!/usr/bin/env python3
"""
🌐 Prometheus Metrics API Provider
Repository Integration: KrypticKode007/kryptic-agent (2026 Framework)

Exposes live Active Inference variables over an embedded HTTP network bus.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class PrometheusMetricsAPI:
    def __init__(self, state, port=8080):
        self.state = state
        self.port = port
        self.server = None

    def start(self):
        state_ref = self.state
        
        class MetricsHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/metrics":
                    self.send_response(200)
                    self.send_header("Content-Type", "text/plain; version=0.0.4")
                    self.end_headers()
                    
                    # Construct Prometheus-compatible gauge telemetry format
                    metrics_payload = (
                        f"# HELP kryptic_hope_level Stabilized system intent metric\n"
                        f"kryptic_hope_level {state_ref.hope_level}\n"
                        f"# HELP kryptic_exhaustion Accumulated operational wear profiles\n"
                        f"kryptic_exhaustion {state_ref.exhaustion}\n"
                        f"# HELP kryptic_variational_free_energy Real-time informational prediction error\n"
                        f"kryptic_variational_free_energy {state_ref.variational_free_energy:.6f}\n"
                        f"# HELP kryptic_somatic_precision Sensory confidence mapping scalar\n"
                        f"kryptic_somatic_precision {state_ref.somatic_precision:.4f}\n"
                    )
                    self.wfile.write(metrics_payload.encode('utf-8'))
                else:
                    self.send_response(404)
                    self.end_headers()

            def log_message(self, format, *args):
                return  # Mute terminal server standard log noise

        try:
            self.server = HTTPServer(("127.0.0.1", self.port), MetricsHandler)
            self.server.serve_forever()
        except Exception:
            pass

    def stop(self):
        if self.server:
            self.server.shutdown()
                    
