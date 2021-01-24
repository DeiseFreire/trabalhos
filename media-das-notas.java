
import javax.swing.JOptionPane;

/*
 * Fontes da ideia:
 *
 * JAVA Sistema média de aluno parte 1. Produção de Edijovem.  
 * Publicado pelo canal Edijovem. [S. l.], 2016. 2 videoaulas (9 mins. 17 segs.). Youtube.
 *
 * JAVA Sistema média de aluno parte 2. Produção de Edijovem.  
 * Publicado pelo canal Edijovem. [S. l.], 2016. 2 videoaulas (4 mins. 21 segs.). Youtube.
 */

/**
 *
 * @author deise
 */
public class bimestre {

    public static void main(String[] args) {
        String nome;
        float n1, n2, n3, n4, media = 0;
        nome = JOptionPane.showInputDialog(null, "Digite o nome do aluno");
        n1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Digite a primeira nota"));
        n2 = Float.parseFloat(JOptionPane.showInputDialog(null, "Digite a segunda nota"));
        n3 = Float.parseFloat(JOptionPane.showInputDialog(null, "Digite a terceira nota"));
        n4 = Float.parseFloat(JOptionPane.showInputDialog(null, "Digite a quarta nota"));
        media = ((n1 + n2 + n3 + n4) / 4);
        JOptionPane.showInternalMessageDialog(null, " A média do aluno " + nome + " é " + media);

    }
}
