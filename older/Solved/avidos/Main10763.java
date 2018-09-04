package avidos;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main10763 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		  
	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

	    int tamanio=1;
	    while ( tamanio!=0){
	    	tamanio=in.nextInt();
	    	if(tamanio==0){
	    		break;
	    	}
	    	int [] arr1 = new int[tamanio];
	    	int [] arr2 = new int[tamanio];

	    	
	    	
	    	
	    	for(int i=0;i<tamanio;i++){
	    		arr1[i]=in.nextInt();
	    		arr2[i]=in.nextInt();

				
			}
	    	
	    	Arrays.sort(arr1);
	    	Arrays.sort(arr2);
	    	
	    	if (Arrays.equals(arr1,arr2)){
	            System.out.println("YES");

	    	}
	        else{
	            System.out.println("NO");

	        }
			

			
	  
	    }
	    
		
		
	}

}
