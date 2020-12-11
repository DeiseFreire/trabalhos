/*
 * Crie as classes Pessoa e Endereco e faça o que se pede:
 * 1 - Na classe Endereco, insira os atributos logradouro, numero, complemento, bairro, cidade e CEP. Crie um construtor vazio e outro para inicializar todos os atributos da classe.
 * 2 - Na classe Pessoa, insira os atributos nome, CPF, e endereço (associação da classe Endereco). Crie um construtor vazio e outro para inicializar todos os atributos da classe.
 * 3 - Crie um método, em cada classe do exemplo, para retornar uma String que apresente o conteúdo de todos os atributos;
 * 4 - Implemente o método main para apresentar o contexto referente aos itens acima.
 */

/**
 *
 * JAVA: Orientado a objetos classe pessoa. Produção de [s. N.]. [S. L.]: Publicado
 * Pelo Canal Webforcraft Java, 2013. 1 vídeo (12min.17seg.), color. Youtube.
 */
import javax.swing.*;

public class Pessoa {

    public static void main(String[] args) {
        Pessoa p = new Pessoa();
        p.nome = JOptionPane.showInputDialog(null, "Digite o nome da pessoa");
        p.cpf = JOptionPane.showInputDialog(null, "Digite o CPF " + p.getNome());
        p.endereco = JOptionPane.showInputDialog(null, "Digite seu endereço " + p.getNome());
        p.logradouro = JOptionPane.showInputDialog(null, "Digite o logradouro " + p.getNome());
        p.numero = JOptionPane.showInputDialog(null, "Digite o numero " + p.getNome());
        p.complemento = JOptionPane.showInputDialog(null, "Digite o complemento " + p.getNome());
        p.bairro = JOptionPane.showInputDialog(null, "Digite o bairro " + p.getNome());
        p.cidade = JOptionPane.showInputDialog(null, "Digite a cidade " + p.getNome());
        p.cep = JOptionPane.showInputDialog(null, "Digite o cep " + p.getNome());
        JOptionPane.showMessageDialog(null, "Nome: " + p.getNome() + "\n" + "CPF: " + p.getCPF() + "\n" + "Endereço: " + p.getEndereco() + "\n" + "Logradouro: " + p.getLogradouro() + "\n" + "Numero: " + p.getNumero() + "\n" + "Complemento: " + p.getComplemento() + "\n" + "Bairro: " + p.getBairro() + "\n" + "Cidade: " + p.getCidade() + "\n" + "Cep: " + p.getCep());
    }
//public static class Endereco {
    public String nome;
    private String cpf;
    private String endereco;
    public String logradouro;
    public String numero;
    public String complemento;
    public String bairro;
    public String cidade;
    private String cep;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCPF() {
        return cpf;
    }

    public void setCPF(String cpf) {
        this.cpf = cpf;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getComplemento() {
        //String complemento = null;
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public String getBairro() {
        //String complemento = null;
        return complemento;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;

    }

    private String getCep() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

}
