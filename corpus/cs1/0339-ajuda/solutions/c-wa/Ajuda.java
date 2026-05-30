import java.util.Scanner;
import java.util.ArrayList;

public class Ajuda {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean continuar = true;
		while (continuar) {
			int tamanho = sc.nextInt();
			if (tamanho != 0) {
				String[] letra = new String[tamanho];
				int[] tempo = new int[tamanho];
				String[] acerto = new String[tamanho];
				for (int i = 0; i < tamanho; i++) {
					letra[i] = sc.next();
					tempo[i] = sc.nextInt();
					acerto[i] = sc.next();
				}
				int tempoTotal = 0;
				int qtdAcertos = 0;
				for (int i = 0; i < tamanho; i++) {
					if (letra[i].equals("Pass")) {
						continue;
					}
					if (acerto[i].equals("correct")) {
						tempoTotal += tempo[i];
						qtdAcertos += 1;
						for (int j = 0; j < tamanho; j++) {
							if (i == j) {
								continue;
							}
							if (letra[i].equals(letra[j])) {
								if (!acerto[j].equals(" correct")) {
									tempoTotal += 20;
									letra[j] = "Pass";
								}
							}
						}
					}
				}
				System.out.println(qtdAcertos + " " + tempoTotal);
			} else {
				continuar = false;
			}

		}
	}
}
