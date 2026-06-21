/* Crie um algoritmo em Java que mostre na tela todos os múltiplos de 3 entre os números
0 e 30 usando a estrutura “do while".
 */


public class Ex3 {
    public static void main (String[]args) {

        int multiplo = 0;

        do {
            if (multiplo % 3 == 0) {
                System.out.println(multiplo);
            }

            multiplo ++;

        } while (multiplo <= 30);

        }
    }
