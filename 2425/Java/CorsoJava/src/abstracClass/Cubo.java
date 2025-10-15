package abstracClass;

class Cubo extends Figura{
    private int lato;
    Cubo()
    {
        lato=0;
        alt=0;
    }//costruttore di deault

    Cubo(int l,int h)
    {
        lato=l;
        alt=h;
    }//costruttore

    public double area(){return lato*lato;}
}//fine classe Para