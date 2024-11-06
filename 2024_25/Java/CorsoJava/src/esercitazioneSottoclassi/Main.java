package esercitazioneSottoclassi;


public class Main {
    public static void main(String[] args) {
        Persona pippo = new Persona();
        pippo.visualizza();

        System.out.println();
        Persona pluto = new Persona("Pluto", "Predazzo");
        pluto.visualizza();

        System.out.println();
        Studente studente1 = new Studente("Black Jack", "Cavalese");
        studente1.visualizza();

        System.out.println();
        System.out.println("Before");
        System.out.println("Piano di studio: " + studente1.getPdS());
        studente1.modificaPdS("INF");

        System.out.println();
        System.out.println("After");
        System.out.println("Piano di studio: " + studente1.getPdS());
    }
}
