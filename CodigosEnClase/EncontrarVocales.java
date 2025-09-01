import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
public class EncontrarVocales {
    public static void main(String[] args) {
        Encontrar();
    }
    public static void Encontrar(){
        String[] Vocales = {"a","e","i","o","u"};
        List<String> Vocal = Arrays.asList(Vocales);
        String[] NoVocales = {"b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"};
        List<String> NoVocal = Arrays.asList(NoVocales);
        Scanner sc = new Scanner(System.in);
        Boolean continua = true;
        while (continua) {
            System.out.println("Ingrese la palabra que quiere escanear y no olvidar que para salir debe usar \"Exit\"!");
            String opc = sc.next().toLowerCase();
            int VocCant = 0;
            int NoVocCant = 0;
            ArrayList<String> Voc = new ArrayList<>();
            ArrayList<String> NoVoc = new ArrayList<>();
            if(opc.contains("Exit")){
                continua = false;
            }
            for (int i = 0; i < opc.length();i++){
                char letra = opc.charAt(i);
                String letr = String.valueOf(letra);
                if(Vocal.contains(letr)){
                    Voc.add(letr);
                    VocCant ++;
                }else if(NoVocal.contains(letr)){
                    NoVoc.add(letr);
                    NoVocCant ++;
                }
            }
            
            System.out.println("La palabra contiene " + VocCant + " Vocales y contiene " + NoVocCant + " No Vocales");
            System.out.println("Las Vocales que contienes son: " + Voc + "\nLas No Vocales que contiene son: " + NoVoc);
        }
    }
}