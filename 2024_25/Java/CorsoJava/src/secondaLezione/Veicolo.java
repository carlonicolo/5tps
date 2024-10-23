package secondaLezione;

/**
 * Classe Veicolo
 * Secondo esempio del corso Java 4INF
 */
public class Veicolo {
    // questo è un commento in linea

    // attributi della classe
    // [accessibilità] [tipo] [nome] = [valore]
    private int anno_immatricolazione;
    private String alimentazione;
    private String marca;

    public Veicolo(int anno_immatricolazione, String alimentazione, String marca) {
        this.anno_immatricolazione = anno_immatricolazione;
        this.alimentazione = alimentazione;
        this.marca = marca;
    }

    public int getAnno_immatricolazione() {
        return anno_immatricolazione;
    }

    public void setAnno_immatricolazione(int anno_immatricolazione) {
        this.anno_immatricolazione = anno_immatricolazione;
    }

    public String getAlimentazione() {
        return alimentazione;
    }

    public void setAlimentazione(String alimentazione) {
        this.alimentazione = alimentazione;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "Veicolo{" +
                "anno_immatricolazione=" + anno_immatricolazione +
                ", alimentazione='" + alimentazione + '\'' +
                ", marca='" + marca + '\'' +
                '}';
    }
}
