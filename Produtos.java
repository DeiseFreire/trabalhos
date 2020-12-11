
/* 
* 1 – 4 - LISTA DE EXERCÍCIO 
* Exercício 4
* Identifique as classes e implemente um programa para a seguinte 
* especificação: “O supermercado vende diferentes tipos de produtos. Cada 
* produto tem um preço e uma quantidade em estoque. Um pedido de um 
* cliente é composto de itens, onde cada item especifica o produto que o 
* cliente deseja e a respectiva quantidade. Esse pedido pode ser pago em 
* dinheiro, cheque ou cartão.”
* 
*/

import javax.swing.JOptionPane;

/**
*
* FONTE DA IDEIA:
* EXERCÍCIO 01 em java: Simulando um supermercado. Canal: Cursos Wl. 
* Brasil: Wilker, 2016. Duração (17'43"), color. Youtube.
 */
public class Produtos {

    public String nome;
    public int quantidade;
    public String unidadeMedida;
    public double preco;

    public void exibirProduto() {
        JOptionPane.showMessageDialog(null, "Nome do produto: " + nome + "\nQuantidade: " + quantidade + "\nUnidade de Medida: " + unidadeMedida + "\nPreço: " + preco);

    }
    public class Supermercado {

    public static void main(String[] args) {

        Produtos produto1 = new Produtos();
        produto1.nome = "Café";
        produto1.quantidade = 10;
        produto1.unidadeMedida = "Kg";
        produto1.preco = 25.00;
        produto1.exibirProduto();

    }
}

