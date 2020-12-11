
/**
 *
 * @author deise
 */
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
