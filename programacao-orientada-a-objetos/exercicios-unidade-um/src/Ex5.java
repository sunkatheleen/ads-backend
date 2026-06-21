/* Crie um algoritmo em Java que peça ao usuário para que se digite um ano (exemplo: 2032).
Em seguida, o algoritmo deve verificar se o ano informado é ou não bissexto
 */

import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite um ano (ex: 2024) para descobrir se ele é bissexto ou não:");
        int ano = scanner.nextInt();

        if ((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0) {
            System.out.println("O ano é bissexto.");
        }
        else {
                System.out.println("O ano não é bissexto.");
            }
        }

    }
