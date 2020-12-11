
import java.util.Scanner;

/*
* Crie uma classe Calculadora que tenha três * atributos (valor1, valor2, valor3), posteriormente faça o que se pede:
* 1.     Crie um construtor para inicializar o atributo valor1
* 2.     Crie outro construtor para inicializar os atributos valor1 e valor2;
* 3.     Crie um terceiro construtor para inicializar os atributos valor1, valor2 e valor3;
* 4.     Crie um método, sem parâmetros, que retorne a soma de todos os atributos.
* 5.     Crie um método, sem parâmetros, que retorne a subtração de todos os atributos.
* 6.     Crie um método, sem parâmetros, que retorne a divisão de todos os atributos.
* 7.     Crie um método, sem parâmetros, que retorne a multiplicação de todos os atributos.
* 8.     Implemente o método main para apresentar o contexto referente aos itens acima.
 */

/**
 * FONTE DA IDEIA: 
 * CALCULADORA com orientação à objetos (java).
 * Direção de Willian Barata. Produção de Willian Barata. Brasil: Youtube, 2018.
 * 1 Vídeo (10min.37seg.), color.
 *
 */
public class CalculadoraComObjetos {

    public static void main(String[] args) {
        double valor1, valor2, valor3;

        System.out.println("Digite o primeiro número: ");
        Scanner leia = new Scanner(System.in);

        valor1 = leia.nextDouble();
        System.out.println("Digite o segundo número: ");

        valor2 = leia.nextDouble();
        Operacao result = new Operacao();

        valor3 = result.soma(valor1, valor2);
        System.out.println("A soma é : " + valor3);

        valor3 = result.subtracao(valor1, valor2);
        System.out.println("A subtracao é: " + valor3);

        valor3 = result.divisao(valor1, valor2);
        System.out.println("A divisão é : " + valor3);

        valor3 = result.multiplicacao(valor1, valor2);
        System.out.println("A multiplicação é: " + valor3);
    }
}
