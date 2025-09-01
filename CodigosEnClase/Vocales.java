import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
public class Vocales{
    public static void main(String[] args) {
        Integer x = 0;
        Integer z = 0;
        Integer y = 0;
        String[] Vocales = {"a","e","i","o","u"};
        List<String> Vocal = Arrays.asList(Vocales);
        Scanner sc = new Scanner(System.in);
        String opc = "Hola";
        while (z != 1){
            opc = sc.next();
            if (opc.contains("Exit")){
                z = 1;
                System.out.println("Vocales: " + x);
                System.out.println("No Vocales: " + y);
            }
            if (Vocal.contains(opc.toLowerCase())){
                x ++;
            }
            else{
                y ++;
            }
        }
    }
}