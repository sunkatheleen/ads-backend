package Contas;

public class Banco {
    public static void main(String[] args) {
        // Cria objetos da classe Conta
        Conta cta1 = new Conta();
        Conta cta2 = new Conta();

        cta1.setSaldo(1000.50);
        cta1.setDono("Katheleen");

        cta2.setSaldo(5000.00);
        cta2.setDono("Gabryel");

        System.out.println("Cta 1 - Correntista: " + cta1.getDono());
        System.out.println("Cta 1 - Saldo: " + cta1.getSaldo());

        System.out.println("Cta 2 - Correntista: " + cta2.getDono());
        System.out.println("Cta 2 - Saldo: " + cta2.getSaldo());
    }
}
