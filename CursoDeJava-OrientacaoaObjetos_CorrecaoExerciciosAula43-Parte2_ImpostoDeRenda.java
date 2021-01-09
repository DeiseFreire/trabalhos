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
public class PessoaFisica extends Contribuinte {

    private String cpf;

    /**
     * @return the cpf
     */
    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    @Override
    public double calcularImposto() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
public class PessoaJuridica extends Contribuinte {

    private String cnpj;

    public String getCnpj() {
        return cnpj;
    }

    @Override
    public double calcularImposto() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
