/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package bdlibrosg70;

import java.sql.*;

public class Conexion {
    Connection conectar=null;
    
    public Connection conectar(){
        
        try {
            Class.forName("org.sqlite.JDBC");
            conectar=DriverManager.getConnection("jdbc:sqlite:librosG70.db");
            
            
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return conectar;
    }
}
