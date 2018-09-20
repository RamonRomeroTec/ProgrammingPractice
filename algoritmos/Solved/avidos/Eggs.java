package avidos;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

//11900

public class Eggs {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		

		  
	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));

	    int casos=in.nextInt();
	    int i;
	    for(i=0; i<casos; i++){
	    	int tothuevos= in.nextInt();
	    	int limhuevos=in.nextInt();
	    	int limPeso=in.nextInt();
	    	int [] huevos = new int[tothuevos];

	    	for(int j=0; j<tothuevos; j++){
	    		huevos[j]=in.nextInt();

	    	}
	    	Arrays.sort(huevos);
	    	int sum=0;
	    	int c=0;
	        
	        for(int k = 0;(k<tothuevos && k<limhuevos) && sum<=limPeso;++k){
	        	sum=sum+huevos[k];
	        	if(sum<=limPeso){
	        		c++;
	        	}
	            
	        }
	        
	       

	        
	        System.out.println("Case "+(i+1)+": "+c);
	    }
	    	

	}

}
