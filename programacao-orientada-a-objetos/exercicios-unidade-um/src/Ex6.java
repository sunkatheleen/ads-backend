/*Crie um algoritmo em Java que solicita um número inteiro ao usuário. Em seguida, deve-se
verificar se o número digitado é ou não é um número primo.
 */

import java.util.Scanner;

public class Ex6 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Insira um número inteiro para verificarmos se ele é um número primo:");
        int numero = scanner.nextInt();

        if (numero < 2) {
            System.out.println("O número não e primo.");
        } else {
            boolean primo = true;
            for (int i = 2; i <= Math.sqrt(numero); i++) {
                if (numero % i == 0) {
                    primo = false;
                    break;
                }
            }
            if (primo){
                System.out.println("O número é primo.");
            }
            else {
                System.out.println("O número não é primo.");
            }
        }
    }
}
