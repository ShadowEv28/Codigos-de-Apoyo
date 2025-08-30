import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Calculos {
ArrayList <String> error = new ArrayList<>();
    void Calc(){
        String[] dia = {"Lunes","Martes","Miercoles","Jueves","Vienres","Sabado","Domingo"};
        Scanner sc = new Scanner(System.in);
        ArrayList <Integer> ventas = new ArrayList<>();
        Integer venta = 0;
        List<String> dias = Arrays.asList(dia);
        System.out.println("\n//////////////////////////////////\nRecordar que al ingresar ventas no se aceptaran datos que no sean numeros enteros!");
                    Integer Promedio = 0;
                    for(Integer i = 0; i < dias.size(); i++){
                        try{
                            System.out.println("Ingrese las ventas del dia " + dias.get(i) + ":");
                            venta = sc.nextInt();
                            ventas.add(venta);
                            Promedio += venta;

                        }catch(InputMismatchException e){
                            System.err.println("Ingrese un valor correcto!");
                            error.add("Se intento ingresar el dato " + venta + " En Ingresar Ventas");
                            sc.next();
                            i--;
                            continue;
                        }
                    }
                    Promedio = Promedio/7;
                    Collections.sort(ventas);
                    System.out.println("\n////////////////////////////////// \n--Ventes de la semana--\nPeor Dia: " + ventas.get(0) + "$\nMejor Dia: " + ventas.get(6) + "$\nPromedio de ventas: " + Promedio + "$\n" );
                    ventas.clear();
    }  
}
