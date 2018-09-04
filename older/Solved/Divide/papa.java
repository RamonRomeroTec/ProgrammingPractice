package divideConquista;

//857
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class papa {

	public static void main(String[] args) {

	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		 int anios;

		 while (in.hasNext()){
		 anios=in.nextInt();
		        anios--;
		
		
		int npapas=in.nextInt();
		int[] papas = new int[npapas];
		for ( int i = 0; i < npapas; i++ ){
			papas[i]=in.nextInt();
		}
		   int contador = 0;
	       int j=0;
	       int first=0;
	       int last=0;
	       int max = 0;

	       for ( int i = 0; i < npapas; i++ ) {
	            j = i;
	           contador = 0;
	           while (j<npapas && papas [j] <= papas [i] + anios) {
	               j++;
	               contador++;
	           }

	           if ( contador > max ) {
	               max = contador;
	               first = papas[i];
	               last = papas[j - 1];
	           }
	       }
		
	       System.out.println(max+" "+first+" "+ last);

		    }
		
	}

}
