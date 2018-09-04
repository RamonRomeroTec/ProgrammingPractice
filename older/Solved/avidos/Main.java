package avidos;

//10656

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		  
	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

	    int tamanio=1;
	    while ( tamanio!=0){
	    	tamanio=in.nextInt();
	    	if(tamanio==0){
	    		break;
	    	}
	    	int [] arr = new int[tamanio];
	    	
	    	
	    	
	    	for(int i=0;i<tamanio;i++){
	    		arr[i]=in.nextInt();
				
			}

			
	    	boolean lista = false;
			for ( int i = 0 ; i < tamanio; i++  ){
				if ( arr[i] > 0 ) {
					if ( lista == true) {
						System.out.print(" ");
					}
					System.out.print(arr[i]);
					lista = true;
				}
			}
			if ( lista==false ){
				System.out.print("0");
			}
			
			System.out.print("\n");

				
		
	    	
	  
	    }
	    
	    
	    
	}

}
