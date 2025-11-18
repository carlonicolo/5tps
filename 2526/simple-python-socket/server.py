#!/usr/bin/env python3
"""
Server TCP semplice (multi‑client) per Windows.
- Avvia:   py server.py --host 0.0.0.0 --port 5000
- Client:  py client.py --host 127.0.0.1 --port 5000
Protocollo testuale (una riga = un comando):
  - ECHO <testo>    → restituisce <testo>
  - TIME            → ora del server
  - EXIT            → chiude la connessione
Qualsiasi altro comando → "ERROR"
"""
import argparse, socket, threading, datetime

def handle_client(conn, addr):
    print(f"[+] Connesso: {addr}")
    with conn:
        conn.sendall(b"OK SimpleServer v1\r\n")
        f = conn.makefile("rwb", buffering=0)
        while True:
            line = f.readline()
            if not line:
                break
            try:
                msg = line.decode("utf-8").strip()
            except UnicodeDecodeError:
                f.write(b"ERROR invalid encoding\r\n")
                continue
            if not msg:
                continue
            parts = msg.split(" ", 1)
            cmd = parts[0].upper()
            if cmd == "ECHO" and len(parts) == 2:
                f.write((parts[1] + "\r\n").encode("utf-8"))
            elif cmd == "TIME":
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write((now + "\r\n").encode("utf-8"))
            elif cmd == "EXIT":
                f.write(b"OK bye\r\n")
                break
            else:
                f.write(b"ERROR\r\n")
    print(f"[-] Disconnesso: {addr}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=5000)
    args = p.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((args.host, args.port))
        s.listen(5)
        print(f"[server] In ascolto su {args.host}:{args.port}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()
