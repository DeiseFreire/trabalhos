/*
 * Fonte da ideia:
 * AULA 37: Classe Contador em Java. Produção de professor Takuno. Publicado pelo canal de professor 
 * Takuno. [S.l: s.n.], 2017. 1 videoaula. (11 min. 04 segs.). Youtube.
 */

/**
 *
 * @author deise
 */
public class ContadorDePessoas {

    public static void main(String[] args) {
        limitePessoas c1 = new limitePessoas(40);

        c1.registraEntrada(1);

        System.out.println(c1.getRestaurante());
        System.out.println("O restaurante ultrapassou o limite máximo permitido de pessoa que é de 40 pessoas! ");

    }
}

public class limitePessoas {

    private int restaurante;

    public limitePessoas() {
        restaurante = 0;
    }

    public limitePessoas(int qtdePresentes) {
        restaurante = qtdePresentes;
    }

    public void registraEntrada() {
        restaurante++;
    }

    public void registraEntrada(int delta) {
        restaurante = restaurante + delta;
    }

    public void registraSaida() {
        restaurante--;

    }

    int getRestaurante() {
        return restaurante;
    }
}
