/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo.DAO;

import bdlibrosg70.Conexion;
import java.sql.*;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Usuario
 */
public class ActualizarUnidades {
    
    public void actualizarU(int isbn, int cantidad){
        
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            Statement st = cn.createStatement();
            
            ResultSet rs = st.executeQuery("SELECT * FROM libro WHERE ISBN='" + isbn + "'");

            if (rs.next()) {
                ResultSet rsi = st.executeQuery("SELECT * FROM inventario WHERE ISBN='" + isbn + "'");

                if (rsi.next()) {
                    PreparedStatement ps = cn.prepareStatement("UPDATE inventario SET cantidad=? WHERE ISBN=?");
                    ps.setInt(1, rsi.getInt(2)+cantidad);
                    ps.setInt(2, isbn);
                    ps.executeUpdate();
                    ps.close();
                    System.out.println("Unidades Actualizadas exitosamente");
                }else{
                    PreparedStatement ps = cn.prepareStatement("INSERT INTO inventario VALUES(?,?)");
                    ps.setInt(1, isbn);
                    ps.setInt(2, cantidad);
                    ps.executeUpdate();
                    System.out.println("Unidades Insertadas exitosamente");
                    ps.close();
                }
                rs.close();   
            }else{
                System.out.println("No existe un libro con ese ISBN"); 
            }
            cn.close();
            
            
            
        } catch (SQLException ex) {
            Logger.getLogger(ActualizarUnidades.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
    }
}
