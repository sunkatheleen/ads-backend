/* Crie um algoritmo em Java que peça ao usuário para que se digite um número inteiro
(exemplo: 14). Em seguida, o algoritmo deve mostrar a tabuada do número digitado utilizando o “for”.
 */

import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um número inteiro:");
        int numero = scanner.nextInt();

        for (int i = 1; i <= 10; i++) {
            int resultado = numero * i;
            System.out.println("A tabuada do " + numero + " é: " + numero + " x " + i + " = " + resultado);
    }
    }
}
