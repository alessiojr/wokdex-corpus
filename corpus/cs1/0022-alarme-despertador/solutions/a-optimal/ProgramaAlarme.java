import java.util.Scanner;

public class ProgramaAlarme {

    public static void main(String[] args) {
        Alarme alarme = new Alarme();
        Scanner sc = new Scanner(System.in);
            
        int h1, m1, h2, m2 ;
        do{
            h1 = sc.nextInt();
            m1 = sc.nextInt();
            h2 = sc.nextInt();
            m2 = sc.nextInt();
            
            alarme.setHoraAtual(sc.nextInt(), sc.nextInt());
            alarme.setHoraDesperta(sc.nextInt(), sc.nextInt());

            System.out.println(alarme.QuantasMinutosDespertar());
        }while((h1 == 0) && (h2 == 0) && (m1 == 0) && (m2 == 0));
        
    }

}