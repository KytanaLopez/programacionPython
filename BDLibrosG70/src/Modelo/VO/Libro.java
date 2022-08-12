/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo.VO;

/**
 *
 * @author Usuario
 */
public class Libro {
    //Value Object
    
    private int isbn;
    private String titulo;
    private int año;

    public Libro() {
    }

    public Libro(int isbn, String titulo, int año) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.año = año;
    }

    public int getIsbn() {
        return isbn;
    }

    public void setIsbn(int isbn) {
        this.isbn = isbn;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getAño() {
        return año;
    }

    public void setAño(int año) {
        this.año = año;
    }

   
}
