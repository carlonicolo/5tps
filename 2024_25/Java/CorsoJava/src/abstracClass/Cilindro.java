package abstracClass;

class Cilindro extends Figura{
    private int ray;

    Cilindro(){
        ray=0;
        alt=0;
    }//costruttore di deault

    Cilindro(int r,int h) {
        ray=r;
        alt=h;
    }//costruttore

    public double area()
    {
        return ray*ray*Math.PI;
    }
}//fine classe Cyl

