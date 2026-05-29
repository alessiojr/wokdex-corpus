public class Alarme {

    private int h1, m1;
    private int h2, m2;
    private int r;

    public Alarme() {
        this.h1 = 0;
        this.m1 = 0;
        this.h2 = 12;
        this.m2 = 0;
    }
    
    public int geth1() {
        return h1;
    }

    public int getm1() {
        return m1;
    }

    public int geth2() {
        return h2;
    }

    public int getm2() {
        return m2;
    }

    public void setHoraAtual(int hora, int minuto) {
        h1 = hora;
        m1 = minuto;
    }

    public void setHoraDesperta(int hora, int minuto) {
        h2 = hora;
        m2 = minuto;
    }

    public int QuantasMinutosDespertar() {            

        if (h1 != 0 || m1 != 0 || h2 != 0 || m2 != 0) {
            h1 = h1 * 60;
            h2 = h2 * 60;
            m1 = m1 + h1;
            m2 = m2 + h2;

            if (m1 > m2) {
                r = m1 - m2;
                r = 1440 - r;
            } else {
                r = m2 - m1;
            }
        }   
        
        return r;    
    }   

}