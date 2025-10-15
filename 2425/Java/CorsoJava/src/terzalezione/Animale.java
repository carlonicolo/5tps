package terzalezione;

public class Animale {
    private int eta;
    private int numero_zampe;
    private float peso;
    private String nome;
    private boolean maggiorenne;

    public Animale(int eta, int numero_zampe){
        this.eta = eta;
        this.numero_zampe = numero_zampe;
    }

    public Animale(int eta, int numero_zampe, float peso, String nome){
        this.eta = eta;
        this.numero_zampe = numero_zampe;
        this.peso = peso;
        this.nome = nome;

        if(this.eta >= 18){
            this.maggiorenne = true;
        }
        else{
            this.maggiorenne = false;
        }
    }

    public int getEta(){
        return eta;
    }

    public int getNumero_zampe(){
        return numero_zampe;
    }

    public float getPeso(){
        return peso;
    }

    public String getNome(){
        return nome;
    }


    public void setEta(int eta) {
        this.eta = eta;
    }

    public void setNumero_zampe(int numero_zampe) {
        this.numero_zampe = numero_zampe;
    }

    public void setPeso(float peso) {
        this.peso = peso;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Animale{" +
                "eta=" + eta +
                ", numero_zampe=" + numero_zampe +
                ", peso=" + peso +
                ", nome='" + nome + '\'' +
                ", maggiorenne=" + maggiorenne +
                '}';
    }
}