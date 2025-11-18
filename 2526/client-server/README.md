# Dockerized Socket Client-Server (KV Store) — FIXED
Questa versione risolve:
1) **Healthcheck**: niente `bash/ss`, si usa Python puro.
2) **Permessi `/data`**: il container server crea `/data` con permessi scrivibili, garantendo la **persistenza** su volume Docker.

## Avvio rapido
```bash
docker compose build
docker compose up -d
docker compose ps
docker logs -f kvserver
```
Dovresti vedere: `Listening on 0.0.0.0:5000` e lo stato **healthy**.

## Uso
```bash
docker compose run --rm client
> SET nome Alice
OK
> GET nome
VALUE Alice
> EXIT
OK bye
```
One‑shot:
```bash
docker compose run --rm client python client.py --cmd "SET x 42"
docker compose run --rm client python client.py --cmd "GET x"
```

## Persistenza
Volume `kvdata` → montato su `/data`. File: `/data/store.json`.
```bash
docker exec -it kvserver sh -lc 'cat /data/store.json'
docker compose restart server
docker compose run --rm client python client.py --cmd "GET x"   # valore ancora presente
```

## Note di sicurezza
Per semplicità il server gira come **root**. In produzione valuta un entrypoint che faccia `chown /data` e poi esegua come utente non‑root.

Buon lavoro!
