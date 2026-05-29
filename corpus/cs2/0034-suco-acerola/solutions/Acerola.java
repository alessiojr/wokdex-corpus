import java.util.Scanner;

public class Acerola {
    public static void main(String[] args) {
        boolean condicao = true;
        Scanner in = new Scanner(System.in);
        while(condicao == true){
            
            int v1 = in.nextInt();
            int v2 = in.nextInt();
            double resultado =0;
            if(v1 != 0 && v2 != 0){
             resultado = v2*50;
             resultado = resultado/1000;
             resultado = resultado/v1;
             System.out.printf("%.2f",resultado);
                condicao = true;
            }else{
                condicao = false;
            }
            
            
        }
        in.close();
        }
}
