# Java Socket — Client/Server Semplici

## Protocollo
- `ECHO <testo>`  → echo
- `TIME`          → ora del server
- `EXIT`          → chiude la connessione

## Compila
```bash
javac Server.java Client.java
```

## Esegui
**Terminale A**
```bash
java Server 5000
```
**Terminale B**
```bash
java Client localhost 5000
```
Esempio:
```
OK SimpleJavaServer v1
> TIME
2025-11-06 12:00:00
> ECHO ciao mondo
ciao mondo
> EXIT
OK bye
```

### One‑shot
```bash
java Client localhost 5000 "ECHO hello"
java Client localhost 5000 "TIME"
```
