package secondaLezione;

import java.io.*;
import java.util.*;

public class VeicoloKevin{
    private int anno_immatricolazione;
    private int alimentazione;
    private String marca;
    private int posizioneX;
    private int posizioneY;
    //movimento
    private int movimentoX;
    private int movimentoY;
    //private String dove;

    private String carArt =
            "       ______\n" +
                    "      //  ||\\ \\\n" +
                    " ____//___||_\\ \\___\n" +
                    " )  _          _    \\\n" +
                    " |_/ \\________/ \\___|\n" +
                    "___\\_/________\\_/_______";

    public VeicoloKevin (int anno_immatricolazione, int alimentazione, String marca,  int posizioneX, int posizioneY, int movimentoX, int movimentoY){
        this.anno_immatricolazione = anno_immatricolazione;
        this.alimentazione = alimentazione;
        this.marca = marca;
        this.posizioneX = posizioneX;
        this.posizioneY = posizioneY;
        this.movimentoX = movimentoX;
        this.movimentoY = movimentoY;
    }
    public VeicoloKevin(int anno_immatricolazione, int alimentazione, int posizioneX, int posizioneY){
        this.anno_immatricolazione = anno_immatricolazione;
        this.alimentazione = alimentazione;
        this.posizioneX = posizioneX;
        this.posizioneY = posizioneY;
    }

    public void getLedCarburante(){
        System.out.println("mancano 20 Litri");
    }

    public int getAnnoImmatricolazione(){
        return this.anno_immatricolazione;
    }
    public void setAnnoImmatricolazione(int annoImmatricolazione){
        this.anno_immatricolazione = annoImmatricolazione;
    }

    public void setMovimentoX(int movimentoX){
        this.posizioneX = posizioneX = movimentoX;
    }

    public int getPosizioneX(){
        return posizioneX;
    }


    public void setMovimentoY(int movimentoY){
        this.posizioneY = posizioneY + movimentoY;
    }
    public int getPosizioneY(){
        return posizioneY;
    }

    public String getCarArt() {
        return carArt;
    }

    public void setCarArt(String indent) {
        this.carArt = String.format("%"+indent+"s%s", "", this.carArt); // Adds 4 spaces
    }

    @Override
    public String toString() {
        return "VeicoloKevin{" +
                "anno_immatricolazione=" + anno_immatricolazione +
                ", alimentazione=" + alimentazione +
                ", marca='" + marca + '\'' +
                ", posizioneX=" + posizioneX +
                ", posizioneY=" + posizioneY +
                ", movimentoX=" + movimentoX +
                ", movimentoY=" + movimentoY +
                '}';
    }
}
