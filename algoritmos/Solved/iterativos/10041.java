/*
 * 
 *
 * Actividad de programación: Problema 10041 de UVA
 * Fecha: 9 de abril de 2017
 * Autor: A01700318 Ramon Romero
 *
 *
 *
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		  
	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	    int casos = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
	    
	    for (int i=0; i< casos; i++){
	    	int familiares= in.nextInt();
		    int[ ]   calles = new  int[familiares];
		    
		    for (int j=0; j<familiares; j++){
		    	calles[j]= in.nextInt();
		    }
		    
		    Arrays.sort(calles);
		    int medium = calles[(calles.length/2)];
		    
		    
		    int dist = 0;
            for (int k = 0; k < familiares; ++k){
            	int s=  Math.abs(medium - calles[k]);
                dist = dist + s;
 
            }
    		    System.out.println(dist);
    		    
	    }
		    
	    }
	    
	    
	    
	    
	    
	

}
