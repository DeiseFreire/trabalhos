/*
 * Fonte da ideia:
 * CURSO de Java - Orientação a Objetos: Correção Exercícios Aula 43 - Parte 2 (Imposto de Renda). 
 * Produção de Loiane Groner. Publicado pelo canal Loiane Groner. [S. l.], 2016. 1 videoaula (25 mins. 48 segs.). 
 * Youtube.
 */
package com.deise.cursojava.aula43.labs.exer02;

/**
 *
 * @author deise
 */
public abstract class Contribuinte {

    private String nome;
    private double rendaBruta;

    /**
     * @return the nome
     */
    public String getNome() {
        return nome;
    }

    /**
     * @param nome the nome to set
     */
    public void setNome(String nome) {
        this.nome = nome;
    }

    /**
     * @return the rendaBruta
     */
    public double getRendaBruta() {
        return rendaBruta;
    }

    /**
     * @param rendaBruta the rendaBruta to set
     */
    public void setRendaBruta(double rendaBruta) {
        this.rendaBruta = rendaBruta;
    }

    public abstract double calcularImposto();
}
