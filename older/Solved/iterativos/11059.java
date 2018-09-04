import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class iter {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		
		 int i,num,k,x,y;

		    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		   while(in.hasNext()){
			   k=in.nextInt();
			   num=0;
		        for(i=k+1; i<=2*k; i++){
		            if((i*k)%(i-k)==0)
		                num++;
		        }
		        System.out.println(num);

		        for(i=k+1; i<=2*k; i++){
		            if((i*k)%(i-k)==0){
		                x=(i*k)/(i-k);
		                y=i;
		                System.out.println("1/"+k+" = 1/"+x+" + 1/"+y);
		            }
		        }
		        
		    }
		   
		
		
		
		
			
		      
		           
		        
		    }
	

}


