public class Persona {
String name = "Ariel ";
Integer Edad = 21;
String nombre;
Integer edad;

    void Saludar(String Nombre){
        System.out.println("Hola, " + Nombre);
        System.out.println(name + Edad);
    }

    Persona(String nombreInicial, Integer edadInicial){
        this.nombre = nombreInicial;
        this.edad = edadInicial;
    }

    void Saluda2(){
        System.out.println("Hola, me llamo " + this.nombre + " y naci el " + (2025 - this.edad));
    }
}

