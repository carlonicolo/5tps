package esercitazioneSottoclassi;

public class Studente extends Persona{
    // Studente eredita variabili e metodi da Persona

    private int matricola;        // Nuova variabile istanza
    private String pianoDiStudio; // Nuova variabile istanza

    // Nuova variabile statica (di classe)
    static int nextMatricola = 1;

    // Costruttore
    public Studente(String nome, String indirizzo) {
        this.nome = nome;               // della superclasse
        this.indirizzo = indirizzo;     // della superclasse
        this.matricola = nextMatricola++;
        this.pianoDiStudio = "";
    }

    // Nuovo metodo
    public String getPdS() {
        return pianoDiStudio;
    }

    // Nuovo metodo
    public void modificaPdS(String nuovoPdS) {
        pianoDiStudio += nuovoPdS + "\n";
    }

    @Override
    public void visualizza() {
        System.out.println("Nome: " + nome + "\nIndirizzo: " + indirizzo + "\nMatricola: " + matricola);
    }

}

