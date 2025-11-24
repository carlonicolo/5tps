import threading
import time


def conta(nome, limite, delay=0.5):
    """Funzione con parametri multipli"""
    for i in range(limite):
        print(f"{nome}: {i}")
        time.sleep(delay)
    print(f"{nome} completato!")


# Argomenti posizionali (args deve essere una tupla)
thread1 = threading.Thread(target=conta, args=("Thread-Alpha", 3), name="T1")

# Argomenti keyword (kwargs è un dizionario)
thread2 = threading.Thread(
    target=conta, kwargs={"nome": "Thread-Beta", "limite": 5, "delay": 0.3}, name="T2"
)

# Mix di args e kwargs
thread3 = threading.Thread(
    target=conta, args=("Thread-Gamma", 4), kwargs={"delay": 0.7}, name="T3"
)

# Avvio tutti i thread
for t in [thread1, thread2, thread3]:
    t.start()

# Attesa completamento
for t in [thread1, thread2, thread3]:
    t.join()
print("Tutti i thread terminati!")
