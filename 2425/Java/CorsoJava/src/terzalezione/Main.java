package terzalezione;

public class Main {
    public static void main(String[] args) {

        // Creo un oggetto di tipo Animale
        // usando uno dei metodi costruttori definiti
        // nella classe Animale
        Animale cane = new Animale(5, 4, 80, "Pippo");
        System.out.println("Ciao mi chiamo " + cane.getNome());

        System.out.println(cane);

        Animale[] zoo = new Animale[2];
        zoo[0] = new Animale(5,5,90,"Jack");
        zoo[1] = new Animale(20,2,70,"Billy");

        for(Animale a : zoo) System.out.println(a);

    }
}