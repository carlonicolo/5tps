import primaLezione.*;
import secondaLezione.*;

public class Main {
    public static void main(String[] args) {
        //System.out.println("Hello world!");
        Animale pluto = new Animale(5,80,4);
        pluto.abbaia();
        String s = pluto.salutaNome("4INF");
        System.out.println(s);

        System.out.println("età pluto prima ");
        System.out.println(pluto.getEta());
        pluto.setEta(8);
        System.out.println("età pluto dopo ");
        System.out.println(pluto.getEta());


        System.out.println("###############");

        Animale zig = new Animale("Zig",5,80,4);
        zig.abbaia();
        String sal = zig.salutaNome("Kevin");
        System.out.println(sal);

        Animale pippo = new Animale("Pluto",18,50,4,"nero");
        pippo.abbaia();
        String pippo_greeting = pippo.salutaNome("ragazzi!!!");
        System.out.println(pippo_greeting);
        System.out.println(pippo.getNome());

        //Veicolo macchina1 = new Veicolo(2023, "elettrica", "Tesla");
        //System.out.println(macchina1);
        //System.out.println("Marca: " + macchina1.getMarca());


    }
}