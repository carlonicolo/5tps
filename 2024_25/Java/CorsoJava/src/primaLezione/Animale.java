package primaLezione;

public class Animale {
    private String nome;
    private int eta;
    private float peso;
    private int num_zampe;
    private String colore;

    public Animale(String nome, int eta, int peso, int num_zampe, String colore) {
        this.nome = nome;
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
        this.colore = colore;
    }

    public Animale(String nome, int eta, int peso, int num_zampe) {
        this.nome = nome;
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
    }

    public Animale(int eta, int peso, int num_zampe) {
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
    }

    public void abbaia(){
        System.out.println("Bau Bau");
    }

    public String salutaNome(String nome){
        String saluto = "Ciao " + nome ;
        return saluto;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getEta() {
        return eta;
    }

    public void setEta(int eta) {
        this.eta = eta;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public int getNum_zampe() {
        return num_zampe;
    }

    public void setNum_zampe(int num_zampe) {
        this.num_zampe = num_zampe;
    }


    public String getColore() {
        return colore;
    }

    public void setColore(String colore) {
        this.colore = colore;
    }
}
