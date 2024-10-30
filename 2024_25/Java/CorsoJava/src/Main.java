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


        // VeicoloKevin

        VeicoloKevin audi = new VeicoloKevin(2000, 20,0,0);
        System.out.println(audi.getAnnoImmatricolazione());
        audi.setAnnoImmatricolazione(2016);
        System.out.println(audi.getAnnoImmatricolazione());
        audi.setMovimentoX(10);
        audi.setMovimentoY(20);
        System.out.println("la posizone X è: " + audi.getPosizioneY());
        System.out.println("" + audi.getPosizioneY());

        System.out.println("la tua audi è in posizione: ");
        System.out.println(audi.toString());

        /*
        System.out.println("*");
        System.out.println(" *");
        System.out.println("  *");
        System.out.println("   *");
        System.out.println("    *");
        System.out.println("     *");
         */

        System.out.println(audi.getCarArt());
        audi.setCarArt("8");
        System.out.println(audi.getCarArt());
    }
}