package abstracClass;

abstract class Figura {
    abstract double area();
    protected int alt;
    public double volume(){
        return alt*area();
    }//fine metodo volume
    public void stampaArea() {
        System.out.println("Area: " + area());
    }//fine metodo stampaArea
    public void stampaVolume() {
        System.out.println("Volume: " + volume());
    }//fine metodo stampaVolume
}//fine classe Figura

