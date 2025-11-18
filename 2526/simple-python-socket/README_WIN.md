# App client/server Python per Windows — Semplice

Due script Python **senza dipendenze esterne**: un **server TCP** e un **client** testuale.
Funziona su Windows (anche PowerShell/Prompt dei comandi).

## 1) Requisiti
- **Python per Windows** (consigliato 3.10+). Verifica:
```
py --version
```

## 2) Avvio rapido (stesso PC)
Apri **due terminali**:

**Terminale A — server**
```
cd windows-simple-python-socket
py server.py --host 0.0.0.0 --port 5000
```
Vedrai: `In ascolto su 0.0.0.0:5000`

**Terminale B — client**
```
cd windows-simple-python-socket
py client.py --host 127.0.0.1 --port 5000
```
Esempio di sessione:
```
OK SimpleServer v1
> TIME
2025-11-05 12:34:56
> ECHO ciao mondo
ciao mondo
> EXIT
OK bye
```

## 3) Modalità one‑shot
Esegui un comando senza entrare in interattiva:
```
py client.py --host 127.0.0.1 --port 5000 --cmd "ECHO hello"
py client.py --host 127.0.0.1 --port 5000 --cmd "TIME"
```

## 4) Test su due PC Windows (stessa LAN)
- Sul PC **server** trova l'IP: `ipconfig` (es. 192.168.1.50) e avvia:
  ```
  py server.py --host 0.0.0.0 --port 5000
  ```
- Sul PC **client**:
  ```
  py client.py --host 192.168.1.50 --port 5000
  ```
> Se Windows Firewall chiede conferma per Python, consenti l'accesso sulla rete privata.

## 5) Personalizzazioni utili
- Porta diversa: `--port 6000`
- Aggiungi un nuovo comando nel server (es. `UPPER <txt>`): nel file `server.py` dentro `handle_client`, aggiungi un `elif`.

## 6) Domande frequenti
- **Errore "Address already in use":** c'è già un server su quella porta → cambia `--port` o chiudi l'altro processo.
- **Il client non si collega da un altro PC:** verifica l'IP, la rete (stessa subnet), la porta sul firewall.

Buona pratica!
