#!/usr/bin/env python3
import os, socket, argparse

def send_cmd(host, port, line):
    with socket.create_connection((host, port), timeout=5) as s:
        f = s.makefile("rwb", buffering=0)
        f.readline()
        f.write((line.strip() + "\n").encode("utf-8"))
        resp = f.readline().decode("utf-8").rstrip()
        return resp

def interactive(host, port):
    with socket.create_connection((host, port), timeout=5) as s:
        f = s.makefile("rwb", buffering=0)
        greet = f.readline().decode("utf-8").rstrip()
        print(greet)
        try:
            while True:
                line = input("> ")
                if not line:
                    continue
                f.write((line.strip() + "\n").encode("utf-8"))
                resp = f.readline().decode("utf-8").rstrip()
                print(resp)
                if line.strip().upper() == "EXIT":
                    break
        except (KeyboardInterrupt, EOFError):
            print("\nbye")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default=os.environ.get("HOST", "server"))
    p.add_argument("--port", type=int, default=int(os.environ.get("PORT", "5000")))
    p.add_argument("--cmd", default=os.environ.get("CMD"))
    a = p.parse_args()
    if a.cmd:
        print(send_cmd(a.host, a.port, a.cmd))
    else:
        interactive(a.host, a.port)

if __name__ == "__main__":
    main()
