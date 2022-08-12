/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo.DAO;

import bdlibrosg70.Conexion;
import java.sql.*;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Usuario
 */
public class VenderLibro {
    
    public void vender(int isbn, int cantidad){
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            Statement st = cn.createStatement();
            
             ResultSet rs = st.executeQuery("SELECT * FROM inventario WHERE ISBN='"+isbn+"'");
            
            if(rs.next()){
                if(rs.getInt(2)>=cantidad){
                    PreparedStatement ps = cn.prepareStatement("INSERT INTO venta VALUES(?,?,?,?)");
                    ps.setInt(1, isbn);
                    //Obtenemos la fecha actual 2022-8-10
                    Calendar fecha = new GregorianCalendar();
                    String año = String.valueOf(fecha.get(Calendar.YEAR));
                    String mes = String.valueOf(fecha.get(Calendar.MONTH)+1);
                    String dia = String.valueOf(fecha.get(Calendar.DAY_OF_MONTH));
                    String fecha_actual = año+"-"+mes+"-"+dia;
                    ps.setString(2, fecha_actual);
                    
                    //Obtener la hora
                    
                    String hora = String.valueOf(fecha.get(Calendar.HOUR_OF_DAY));
                    String minuto = String.valueOf(fecha.get(Calendar.MINUTE));
                    String segundo=String.valueOf(fecha.get(Calendar.SECOND));
                    String hora_actual = hora+":"+minuto+":"+segundo;
                    ps.setString(3, hora_actual);
                    ps.setInt(4, cantidad);
                    ps.executeUpdate();
                    ps.close();
                    
                    //Restar los libros vendidos.. inventario
                    PreparedStatement psI= cn.prepareStatement("UPDATE inventario SET cantidad=? WHERE ISBN=?");
                    psI.setInt(1, rs.getInt(2)-cantidad);
                    psI.setInt(2, isbn);
                    psI.executeUpdate();
                    psI.close();
                    rs.close();
                    
                    System.out.println("Libro vendido con éxito");
                 
                }else{
                    System.out.println("Esa cantidad no está disponible");
                }
            }else{
                System.out.println("No existe ese ISBN en la base de datos");
            }
            cn.close();
            
            
        } catch (SQLException ex) {
            Logger.getLogger(VenderLibro.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
    }
}
