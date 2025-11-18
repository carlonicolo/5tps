#!/usr/bin/env python3
import os, json, threading, socketserver, signal, time

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "5000"))
DATA_FILE = os.environ.get("DATA_FILE", "/data/store.json")
AUTO_FLUSH_SEC = int(os.environ.get("AUTO_FLUSH_SEC", "5"))

store_lock = threading.RLock()
store = {}

def _ensure_dir(path):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)

def load_store():
    global store
    _ensure_dir(DATA_FILE)
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                store.update(json.load(f))
            print(f"[server] Loaded {len(store)} keys from {DATA_FILE}")
        except Exception as e:
            print(f"[server] Warning: could not load store: {e}")
    else:
        save_store()

def save_store():
    tmp = DATA_FILE + ".tmp"
    with store_lock:
        data = json.dumps(store, ensure_ascii=False, indent=2)
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(data)
        os.replace(tmp, DATA_FILE)

class KVHandler(socketserver.StreamRequestHandler):
    def handle(self):
        addr = self.client_address
        print(f"[server] Connection from {addr}")
        self.wfile.write(b"OK Welcome to KVStore v1\n")
        while True:
            line = self.rfile.readline()
            if not line:
                break
            try:
                line = line.decode("utf-8").strip()
            except UnicodeDecodeError:
                self.wfile.write(b"ERROR invalid encoding\n")
                continue
            if not line:
                continue
            parts = line.split(" ", 2)
            cmd = parts[0].upper()
            try:
                if cmd == "SET" and len(parts) == 3:
                    key, value = parts[1], parts[2]
                    with store_lock:
                        store[key] = value
                        save_store()
                    self.wfile.write(b"OK\n")
                elif cmd == "GET" and len(parts) >= 2:
                    key = parts[1]
                    with store_lock:
                        if key in store:
                            val = store[key]
                            out = f"VALUE {val}\n".encode("utf-8")
                            self.wfile.write(out)
                        else:
                            self.wfile.write(b"ERROR not found\n")
                elif cmd == "DEL" and len(parts) >= 2:
                    key = parts[1]
                    with store_lock:
                        if key in store:
                            del store[key]
                            save_store()
                            self.wfile.write(b"OK\n")
                        else:
                            self.wfile.write(b"ERROR not found\n")
                elif cmd == "KEYS":
                    with store_lock:
                        keys = list(store.keys())
                    out = "KEYS " + " ".join(keys) + "\n"
                    self.wfile.write(out.encode("utf-8"))
                elif cmd == "EXIT":
                    self.wfile.write(b"OK bye\n")
                    break
                else:
                    self.wfile.write(b"ERROR unknown or invalid command\n")
            except Exception as e:
                self.wfile.write(f"ERROR {e}\n".encode("utf-8"))
        print(f"[server] Disconnected {addr}")

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

def auto_flush_thread():
    while True:
        time.sleep(AUTO_FLUSH_SEC)
        with store_lock:
            try:
                save_store()
            except Exception as e:
                print(f"[server] Auto-flush error: {e}")

def main():
    load_store()
    af = threading.Thread(target=auto_flush_thread, daemon=True)
    af.start()
    with ThreadedTCPServer((HOST, PORT), KVHandler) as server:
        print(f"[server] Listening on {HOST}:{PORT}, data at {DATA_FILE}")
        def shutdown_handler(signum, frame):
            print("[server] Shutting down...")
            with store_lock:
                save_store()
            server.shutdown()
        signal.signal(signal.SIGTERM, shutdown_handler)
        signal.signal(signal.SIGINT, shutdown_handler)
        server.serve_forever()

if __name__ == "__main__":
    main()
