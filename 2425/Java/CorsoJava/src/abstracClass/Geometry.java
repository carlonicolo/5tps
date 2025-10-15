package abstracClass;

import java.io.*;
import java.util.*;
class Geometry {
    private static BufferedReader stdin=new BufferedReader(new InputStreamReader(System.in));
    public static void main (String args []) {
        Scanner input=new Scanner (System.in);
        int ch,raggio,altezza,lato;
        do{
            System.out.print("Inserisci: \n1 - Cilindro \n2 - Cubo \n0 - per terminare: ");
            ch=input.nextInt();
            switch(ch){
                case 1: System.out.print("ins.raggio per il cerchio di base:");
                    raggio=input.nextInt();
                    System.out.print("ins.altezza del cyl:");
                    altezza=input.nextInt();
                    Cilindro c = new Cilindro(raggio,altezza);
                    c.stampaArea();
                    c.stampaVolume();
                    break;
                case 2: System.out.print("ins.lato per il quadrato di base:");
                    lato=input.nextInt();
                    System.out.print("ins.altezza del para:");
                    altezza=input.nextInt();
                    Cubo p = new Cubo(lato,altezza);
                    p.stampaArea();
                    p.stampaVolume();
                    break;
                default:if(ch!=0)System.out.println("non valido");
            }//fine switch
        }while(ch!=0);
    }//fine main
}// fine classe geo