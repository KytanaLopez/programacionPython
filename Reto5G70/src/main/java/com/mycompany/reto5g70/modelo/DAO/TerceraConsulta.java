/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.reto5g70.modelo.DAO;

import com.mycompany.reto5g70.modelo.VO.Cliente;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author Usuario
 */
public class TerceraConsulta {
     public void terceraconsulta(DefaultTableModel modelo){
        
        Cliente cliente = new Cliente();
        
        try {
            Conexion cc = new Conexion();
            Connection cn = cc.conectar();
            
            Statement st = cn.createStatement();
            
            ResultSet rs = st.executeQuery("SELECT ID_Compra, p.Constructora, p.Banco_Vinculado FROM Compra c JOIN Proyecto p ON (c.ID_Proyecto=p.ID_Proyecto) WHERE Proveedor = 'Homecenter' AND p.Ciudad='Salento'");
            
            
            
            while(rs.next()){
                cliente.setId_compra(rs.getInt(1));
                cliente.setConstructora(rs.getString(2));
                cliente.setBanco(rs.getString(3));
             modelo.addRow(new Object[]{cliente.getId_compra(),cliente.getConstructora(),cliente.getBanco()});
 
            }
            
            
            rs.close();
            cn.close();
            
            
        } catch (SQLException ex) {
            Logger.getLogger(PrimerConsulta.class.getName()).log(Level.SEVERE, null, ex);
        }
    
    }
   
}
