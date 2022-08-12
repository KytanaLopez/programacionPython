/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bdlibrosg70;

import Modelo.DAO.ActualizarUnidades;
import Modelo.DAO.BuscarLibro;
import Modelo.DAO.ConsultarUnidades;
import Modelo.DAO.GuardarLibro;
import Modelo.DAO.ListarLibros;
import Modelo.DAO.VenderLibro;
import Modelo.VO.Inventario;
import Modelo.VO.Libro;
import java.util.Scanner;



/**
 *
 * @author Usuario
 */
public class BDLibrosG70 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc = new Scanner(System.in);
        Libro libro = new Libro();
        Inventario inventario = new Inventario();
        boolean continuar=true;
        
        do {
            System.out.println("Elija la opción a realizar sobre la BD");
            System.out.println("1. Guardar\n"
                    + "2. Buscar\n"
                    + "3. Listar Libros\n"
                    + "4. Actualizar unidades\n"
                    + "5. Consultar unidades\n"
                    + "6. Vender Libro\n"
                    + "7. Salir\n");
            System.out.print("Digite la opción: ");
            int opcion = sc.nextInt();
            switch(opcion){
                case 1: 
                    System.out.println("*************************Guardar Libro********************");
                    System.out.println("Digite el ISBN: ");
                    libro.setIsbn(sc.nextInt());
                    sc.nextLine();
                    System.out.println("Digite el título: ");
                    libro.setTitulo(sc.nextLine());
                    System.out.println("Digite el año de publicación");
                    libro.setAño(sc.nextInt());
                    
                    GuardarLibro guardarL = new GuardarLibro();
                    guardarL.guardar(libro.getIsbn(), libro.getTitulo(), libro.getAño());
                    break;
                    
                case 2:
                    System.out.println("*************************Buscar Libro********************");
                    System.out.println("Digitie el ISBN del libro a buscar");
                    libro.setIsbn(sc.nextInt());
                    BuscarLibro buscarL = new BuscarLibro();
                    buscarL.buscar(libro.getIsbn());
                    break;
                case 3:
                    System.out.println("*************************Listar Libros********************");
                    ListarLibros listarL = new ListarLibros();
                    listarL.listar();
                    break;
                case 4:
                    System.out.println("*************************Actualizar unidades del libro********************");
                    System.out.println("Digite el ISBN del libro a actualizar");
                    libro.setIsbn(sc.nextInt());
                    System.out.println("Digite la cantidad");
                    inventario.setCantidad(sc.nextInt());
                    ActualizarUnidades actualizarUni = new ActualizarUnidades();
                    actualizarUni.actualizarU(libro.getIsbn(), inventario.getCantidad());
                    
                    break;
                case 5:
                    System.out.println("*************************Consultar unidades de libro********************");
                    System.out.println("Digite el ISBN del libro a consultar unidades");
                    libro.setIsbn(sc.nextInt());
                    ConsultarUnidades consultarUni = new ConsultarUnidades();
                    consultarUni.consultarU(libro.getIsbn());
                    break;
                case 6:
                    System.out.println("*************************Vender Libro********************");
                    System.out.println("Digite el ISBN del libro a vender");
                    libro.setIsbn(sc.nextInt());
                    System.out.println("Digite la cantidad a vender");
                    inventario.setCantidad(sc.nextInt());
                    
                    VenderLibro venderL = new VenderLibro();
                    venderL.vender(libro.getIsbn(), inventario.getCantidad());
                    break;
                case 7:
                    System.out.println("Gracias por utilizar nuestro sistema");
                    continuar=false;
                    break;
                default:
                    System.out.println("No es una opción válida");
                    
            }
            
        } while (continuar);
        
       
    }
    
}
