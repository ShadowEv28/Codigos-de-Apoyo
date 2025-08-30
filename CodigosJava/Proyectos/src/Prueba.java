import java.util.InputMismatchException;
import java.util.Scanner;
public class Prueba {
    public static void main(String[] args) throws Exception {
        almacen();
    }

    public static void almacen(){
        Integer opcion = 0;
        Scanner sc = new Scanner(System.in);
        Boolean continua = true;
        while(continua){
            Calculos calc = new Calculos();
            try{
                System.out.println("//////////////////////////////////\n1)Ingresar ventas 👳‍♂️✈🏢🏢\n2)Salir");
                opcion = sc.nextInt();
            switch(opcion){
                case 1:
                    calc.Calc();
                    break;
                case 2:
                    System.out.println("Saliendo del sistema....");
                    continua = false;
                    break;
            }
            }catch(InputMismatchException e){
                System.err.println("Ingrese una opcion valida! ");
                sc.next();
                continue;
            }
        }
    }
}
