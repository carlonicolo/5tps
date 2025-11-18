#!/usr/bin/env python3
"""
Client TCP semplice per Windows.
- Interattivo:   py client.py --host 127.0.0.1 --port 5000
- One-shot:      py client.py --host 127.0.0.1 --port 5000 --cmd "ECHO ciao"
Comandi utili: ECHO <testo>, TIME, EXIT
"""
import argparse, socket, sys

def interactive(host, port):
    with socket.create_connection((host, port), timeout=5) as s:
        f = s.makefile("rwb", buffering=0)
        greeting = f.readline().decode("utf-8", errors="ignore").strip()
        print(greeting)
        while True:
            try:
                line = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                line = "EXIT"
                print()
            if not line:
                continue
            f.write((line + "\r\n").encode("utf-8"))
            data = f.readline()
            if not data:
                print("(connessione chiusa)")
                break
            resp = data.decode("utf-8", errors="ignore").rstrip()
            print(resp)
            if line.upper() == "EXIT":
                break

def oneshot(host, port, cmd):
    with socket.create_connection((host, port), timeout=5) as s:
        f = s.makefile("rwb", buffering=0)
        f.readline()  # greeting
        f.write((cmd.strip() + "\r\n").encode("utf-8"))
        data = f.readline()
        print(data.decode("utf-8", errors="ignore").rstrip())

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=5000)
    p.add_argument("--cmd", default=None, help="comando singolo da inviare (opzionale)")
    a = p.parse_args()
    if a.cmd:
        oneshot(a.host, a.port, a.cmd)
    else:
        interactive(a.host, a.port)

if __name__ == "__main__":
    main()
