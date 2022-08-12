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
public class GuardarLibro {
    public void guardar(int isbn, String titulo, int año){
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            PreparedStatement ps = cn.prepareStatement("INSERT INTO libro VALUES (?,?,?)");
            
            ps.setInt(1, isbn);
            ps.setString(2, titulo);
            
            //Date...
            Calendar fecha= new GregorianCalendar(año,1,1);
            int año_sql = fecha.get(Calendar.YEAR);
            java.sql.Date sqlDate = new java.sql.Date(año_sql);
            ps.setDate(3, sqlDate);
            
            ps.executeUpdate();
            ps.close();
            System.out.println("Libro guardado con éxito");
            cn.close();
            
        } catch (SQLException ex) {
            Logger.getLogger(GuardarLibro.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
        
    }
}
