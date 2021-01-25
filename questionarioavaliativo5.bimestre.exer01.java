/**
* Questão 1
* Uma escola lhe pediu para desenvolver um sistema acadêmico. Em relação ao processo avaliativo, 
* cada bimestre é composto por 3 avaliações que podem ser dos tipos: Prova, Seminário ou Estudo 
* Dirigido. Em entrevista com o responsável pela escola, ficou definido o diagrama de classes abaixo:
* Implemente as classes do Diagrama acima. Em seguida, crie a classe BimestreTesteMain e instancie um 
* bimestre de exemplo composto dos 3 tipos de avaliação existentes e utilize o método imprimirAvaliacoes() 
* para mostra o resultado.
*/
package com.deise.questionarioavaliativo5.bimestre.exer01;


/**
 *
 * @author deise
 */

public class Bimestre {

    Bimestre(Avaliacao av1, Avaliacao av2, Avaliacao av3) {

        this.av1 = av1;
        this.av2 = av2;
        this.av3 = av3;
    }
    private Avaliacao av1;
    private Avaliacao av2;
    private final Avaliacao av3;
    public void imprimirAvaliacoes() {
        System.out.println(av1.getInfo());
        av1.dados();
        System.out.println(av2.getInfo());
        av2.dados();
        System.out.println(av3.getInfo());
        av3.dados();
    }
}
package com.deise.questionarioavaliativo5.bimestre.exer01;

/**
 *
 * @author deise
 */

public abstract class Avaliacao {
    private String nome;
    private double nota;
    public Avaliacao(String nome, Double nota) {
        this.nome = nome;
        this.nota = nota;
    }
    ;
    public abstract void dados();
    public String getInfo() {
        return nome;
    }
    public double getNota() {
        return nota;
    }
}
package com.deise.questionarioavaliativo5.bimestre.exer01;

/**
 *
 * @author deise
 */

public class Prova extends Avaliacao {
    private Double tempoDuracao;
    private int quantidadeDeQuestoes;
    private boolean consultaAutorizada;
    public Prova(String nome, Double nota, double tempo, int qtdQuestoes, boolean consulta) {
        super(nome, nota);
        tempoDuracao = tempo;
        quantidadeDeQuestoes = qtdQuestoes;
        consultaAutorizada = consulta;
    }
    @Override
    public void dados() {
        System.out.print(" Prova: Nota: " + getNota());
        System.out.print(" Tempo: " + tempoDuracao);
        System.out.print(" Quantidade de Questões: " + quantidadeDeQuestoes);
        System.out.println(" Consulta: " + consultaAutorizada);
    }
}

package com.deise.questionarioavaliativo5.bimestre.exer01;

/**
 *
 * @author deise
 */

public class Seminario extends Avaliacao {
    private String tema;
    private Double tempoDuracao;
    public Seminario(String nome, Double nota, Double tempo, String tema) {
        super(nome, nota);
        this.tema = tema;
        tempoDuracao = tempo;
    }
    @Override
    public void dados() {
        System.out.print(" Seminário: Nota: " + getNota());
        System.out.print(" Tema: " + tema);
        System.out.println(" Tempo: " + tempoDuracao);
    }
}

package com.deise.questionarioavaliativo5.bimestre.exer01;

/**
 *
 * @author deise
 */

public class EstudoDirigido extends Avaliacao {
    private String tema;
    private int numeroDePaginas;
    public EstudoDirigido(String nome, Double nota, int numPaginas, String tema) {
        super(nome, nota);
        numeroDePaginas = numPaginas;
        this.tema = tema;
    }
    @Override
    public void dados() {
        System.out.print(" Estudo Dirigido: Nota: " + getNota());
        System.out.print(" Tema: " + tema);
        System.out.println(" Numero de Páginas: " + numeroDePaginas);
    }

}

package com.deise.questionarioavaliativo5.bimestre.exer01;

/**
 *
 * @author deise
 */

public class BimestreTesteMain {
    public static void main(String[] args) {

        Prova av1 = new Prova("deise", 10.0, 10.0, 10.0, "Algoritmos");
        Seminario av2 = new Seminario("deise", 10.0, 10.0, "Matemática Discreta");
        EstudoDirigido av3 = new EstudoDirigido("freire", 10.0, 10.0, "Algebra Linear");
        Bimestre a = new Bimestre(av1, av2, av3);
        a.imprimirAvaliacoes();

    }

}

