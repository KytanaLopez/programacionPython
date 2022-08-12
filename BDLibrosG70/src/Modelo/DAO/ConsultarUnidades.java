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
public class ConsultarUnidades {
    public void consultarU(int isbn){
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            Statement st = cn.createStatement();
            
             ResultSet rs = st.executeQuery("SELECT * FROM inventario WHERE ISBN='"+isbn+"'");
            
            if(rs.next()){
                System.out.println("-----------------------------------------");
                System.out.println("ISBN: "+ rs.getInt(1));
                System.out.println("Cantidad: "+rs.getInt(2));
                System.out.println("------------------------------------------");
                rs.close();
            }else{
                System.out.println("No existen unidades de ese libro o No existe el ISB del libro en la BD");
            }
            cn.close();
        } catch (SQLException ex) {
            Logger.getLogger(ConsultarUnidades.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
}
