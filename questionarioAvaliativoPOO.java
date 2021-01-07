/*
 * Considere o código fonte abaixo representando a classe Animal.
 * public class Animal {
 *
 *  public String nome;
 *  public int quantidadePatas;
 *  public String cor;
 *  public String tipoAlimentacao;
 *
 * }
 */
package model;

/**
 *
 * @author deise
 */
public class Animal {

    public String nome;
    public int quantidadePatas;
    public String cor;
    public String tipoAlimentacao;

}
/*
 * Neste questionário será avaliado a aplicação prática dos conceitos sobre:
 *
 * Encapsulamento;
 * Herança
 * Responda as questões no espaço que se pede ou anexo arquivos com formatos do tipo texto (.doc, .docx, .pdf, etc.) desenvolvendo os algoritmos que se pede.
 * 
 * Considere o código fonte abaixo representando a classe Animal.
 * public class Animal {
 *
 *  public String nome;
 *  public int quantidadePatas;
 *  public String cor;
 *  public String tipoAlimentacao;
 *
 * }
 *
 * Crie uma classe Mamífero que herde da classe Animal e faça o que se pede:
 *
 * Implemente o atributo tipoAlimentacao (String)
 * Crie um método construtor que receba por parâmetro os valores iniciais dos atributos da classe Mamífero e Animal e atribua-os aos seus respectivos atributos.
 * Faça o encapsulamento (métodos get e set) para o atributo tipoAlimentacao .
 * Crie um método dadosMamifero sem parâmetro e do tipo void que quando executado imprima na console os dados do contidos nos atributos da classe Mamifero (incluindo os dados herdados a partir da classe Animal).
 * Cria a classe AnimalMain, implemente o método main para apresentar o nome, cor, quantidadePatas e tipoAlimentação de pelo menos dois animais distrintos.
 *
 */
package model;

public class dadosMamifero extends Animal {

    private String tipoAlimentacao;

    public dadosMamifero(String nome, int quantidadePatas, String cor, String tipoAlimentacao) {
        this.nome = nome;
        this.quantidadePatas = quantidadePatas;
        this.cor = cor;
        this.tipoAlimentacao = tipoAlimentacao;

    }

    dadosMamifero(String camelo, String amarelo, String carnívoro) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    public String getTipoAlimentacao() {
        return this.tipoAlimentacao;
    }

    public void setTipoAlimentacao(String tipoAlimentacao) {
        this.tipoAlimentacao = tipoAlimentacao;
    }

    public void dadosMamifero() {
        String str = "DADOS DO MAMÍFERO:\nNome: " + this.nome + "m\nNúmero de patas: " + this.quantidadePatas + "\nCor: " + this.cor + "\nTipo de Alimentação:  " + this.tipoAlimentacao;

        System.out.println(str);
    }
}
/*
 * A partir do código fonte desenvolvido no exercício anterior, faça o que se pede:
 *
 * 1 - Crie a classe AnimaisMain que contenha um método main  e implemente o algorítimo considerando:.
 * 
 * Crie um objeto camelo do tipo Mamífero e atribua os seguintes valores para seus atributos:
 * Nome: Camelo;
 * Cor: Amarelo;
 * quantidadePatas: 4;
 * tipoAlimentacao: Carnívoro;
 * 
 * b) Crie um objeto tubarao do tipo Peixe e atribua os seguintes valores para seus atributos
 * Nome: Tubarão
 * quantidadePatas: 0
 * Cor: Cinzento
 *
 * c) Crie um objeto ursoCanada do tipo Mamifero e atribua os seguintes valores para seus atributos:
 * Nome: Urso-do-canadá
 * quantidadePatas: 4
 * Cor: Vermelho
 * tipoAlimentacao: Mel
 */

package model;

public class AnimalMain {

    public static void main(String[] args) {

        //(nome,quantidadePatas, cor, tipoAlimentacao)
        dadosMamifero camelo = new dadosMamifero("Camelo", 4, "Amarelo", "Carnívoro");

        //(nome,quantidadePatas, cor, tipoAlimentacao)
        Peixe tubarao = new Peixe("Tubarão", 0, "Cinzento", "Carnívoro");

        //(nome,quantidadePatas, cor, tipoAlimentacao)
        dadosMamifero ursocanada = new dadosMamifero("Urso-do-Canadá", 4, "Vermelho", "Mel");

        camelo.dadosMamifero();

        tubarao.dadosPeixe();

        ursocanada.dadosMamifero();

    }

}
