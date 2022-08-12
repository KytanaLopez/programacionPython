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
public class BuscarLibro {
    public void buscar(int isbn){
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            Statement st = cn.createStatement();
            
            ResultSet rs = st.executeQuery("SELECT * FROM libro WHERE ISBN='"+isbn+"'");
            
            if(rs.next()){
                System.out.println("-------------------------");
                System.out.println("ISBN: "+rs.getInt(1));
                System.out.println("Título: "+rs.getString(2));
                System.out.println("Año: "+rs.getInt(3));
                System.out.println("--------------------------");
                rs.close();
            }else{
                System.out.println("No existe ese ISBN");
            }
            
            cn.close();
            
            
        } catch (SQLException ex) {
            Logger.getLogger(BuscarLibro.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
        
        
        
    }
}
