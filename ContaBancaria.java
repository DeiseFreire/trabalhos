/*
 * Fonte da ideia:
 * CURSO de Java - Orientação a Objetos: Correção Exercícios Aula 43 - Parte 1 (Conta Bancária). Produção de Loiane Groner. Publicado pelo canal de Loiane Groner. 
 * [S. l.], 2016. 1 videoaula (31min. 22segs.). Youtube.
 */

package com.deisefreire;

import java.util.Calendar;
import java.util.Date;

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
public class ContaEspecial extends ContaBancaria {
    
    private double limite;

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    @Override
    public String toString() {
        String s = "ContaEspecial[";
        s += " limite: " + limite;
        s += "; " + super.toString(); 
        s += "]" ;
        return s; 
    }
    
    public boolean sacar(double valor){
        
        double saldoComLimite = this.getSaldo() + limite;
        
        if ((saldoComLimite-valor) >=0){
            this.setSaldo(this.getSaldo()-valor);
            
            //super.sacar(valor);
            return true;
        }
        
        return false;
    }
}

    public class ContaPoupanca extends ContaBancaria {

        private int diaRendimento;

        public int getDiaRendimento() {
            return diaRendimento;
        }

        public void setDiaRendimento(int diaRendimento) {
            this.diaRendimento = diaRendimento;
        }

        @Override
        public String toString() {
            String s = "ContaPoupanca [";
            s += " di: " + diaRendimento;
            s += "numConta: " + numConta;
            s += super.toString();
            s += "]";
            return s;

        }

        public void calcularNovoSaldo(double taxaRendimento) {
            Calendar hoje = Calendar.get.Instance();
            if (diaRendimento == hoje.get(Calendar.DAY_OF_MONTH)) {
                saldo += saldo + taxaRendimento;
                this.setSaldo(this.getSaldo() + (this.getSaldo() * taxaRendimento));
                return true;
            }
            return false;
        }
    }

}


