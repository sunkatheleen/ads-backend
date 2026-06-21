/* Exercício de fixação 1 - Crie um algoritmo em Java que solicita três números
decimais ao usuário. Em seguida, a média destes números é calculada e mostrada na tela
para o usuário.
 */

import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Insira três números decimais para calcularmos a média");

        int i;
        double soma = 0;

        for (i = 0; i < 3; i++) {

            System.out.println("Insira um número:");
            double numero = scanner.nextDouble();
            soma += numero;
        }
        double media = soma/3;
        System.out.println("A média dos números é:" + media);
    }
}


