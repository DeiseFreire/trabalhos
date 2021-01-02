/*
 * Fonte da ideia:
 * CURSO de Java - Orientação a Objetos: Correção Exercícios Aula 43 - Parte 1 (Conta Bancária). Produção de Loiane Groner. Publicado pelo canal de Loiane Groner. 
 * [S. l.], 2016. 1 videoaula (31min. 22segs.). Youtube.
 */
package com.deisefreire;

public class ContaBancaria {
    
    private String nomeCliente;
    private String numConta;
    private double saldo;

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getNumConta() {
        return numConta;
    }

    public void setNumConta(String numConta) {
        this.numConta = numConta;
    }

    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    @Override
    public String toString() {
        String s = "ContaBancaria[";
        s += " nomeCliente: " + nomeCliente;
        s += "; numConta: " + numConta; 
        s += "; saldo: " + saldo;
        s += "]" ;
        return s; 
    }
    
    public void depositar(double valor){
        saldo += valor;
    }
    
    public boolean sacar(double valor){
        if ((saldo-valor) >=0){
            saldo -= valor;
            return true;
        }
        return false;
    }
}
