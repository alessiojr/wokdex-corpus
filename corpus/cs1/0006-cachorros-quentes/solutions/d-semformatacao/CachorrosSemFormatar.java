import java.math.RoundingMode;
import java.util.Scanner;
import java.math.BigDecimal;

public class CachorrosSemFormatar {

    public static void main(String[] args) {
        
        double H=0;
        double P=0;
        double Med;
   
        Scanner sc = new Scanner(System.in);
        
        while(H<1&&P<1){
            H = sc.nextDouble();
            P = sc.nextDouble();
      
            Med = H/P;
            BigDecimal bd = new BigDecimal(Med).setScale(2, RoundingMode.HALF_EVEN);
            System.out.println(bd.doubleValue());
                     
        }          
    }   
}
