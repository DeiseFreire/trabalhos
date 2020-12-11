
/* 
* 
* 1 – 4 - LISTA DE EXERCÍCIO 
*
* Exercício 4
*
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
 * @author deise
 */
public class Produtos {

    public String nome;
    public int quantidade;
    public String unidadeMedida;
    public double preco;

    public void exibirProduto() {
        JOptionPane.showMessageDialog(null, "Nome do produto: " + nome + "\nQuantidade: " + quantidade + "\nUnidade de Medida: " + unidadeMedida + "\nPreço: " + preco);

        /*
*
* Referência usada para fazer o exercício:
* EXERCÍCIO 01 em java: Simulando um supermercado. Canal: Cursos Wl. 
* Brasil: Wilker, 2016. Duração (17'43"), color. Youtube.
         */
    }
}
