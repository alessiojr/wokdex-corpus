
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author aluno
 */
public class LP1_B3_1_SomaDeValores {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int soma = 0;   
        int a = teclado.nextInt();
        soma = soma+a;
        while (a!=0){
            a = teclado.nextInt();
            soma = soma+a;
        }
        System.out.println("A Soma dos valores eh: "+soma);
    }   
}