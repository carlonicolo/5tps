package esercitazioneSottoclassi;

/**
 * Classe Persona
 *
 */
public class Persona {
    String nome;
    String indirizzo;

    public Persona() {
        this("John Doe","ignoto");
    }

    public Persona(String nome) {
        this(nome,"ignoto");
    }

    public Persona(String nome, String indirizzo) {
        this.nome = nome;
        this.indirizzo = indirizzo;
    }

    public String getNome() {
        return nome;
    }

    public String getIndirizzo() {
        return indirizzo;
    }

    public void visualizza() {
        System.out.println("Nome: " + nome + "\nIndirizzo: " + indirizzo);
    }

    public boolean omonimo(Persona p) {
        return this.nome.equalsIgnoreCase(p.nome);
    }
}
