programa
{
	
	funcao inicio()
	{
		inteiro h1, m1, h2, m2, tempo, hora, hora2
	    h1 = 0
	    m2 = 0
	    h1 = 0
	    m2 = 0
        tempo = 0
          
        enquanto(verdadeiro)
        {
            leia(h1)
	        leia(m1)
	        leia(h2)
	        leia(m2)

	     
            hora= h1*60+m1
            hora2 = h2*60+m2
          
            se(h2>h1){
                tempo = hora2 - hora
            } 
            se(h2<h1) {
          	    tempo = 1440+hora2-hora
            }
	    
	        escreva(tempo)
        }
	}
}

