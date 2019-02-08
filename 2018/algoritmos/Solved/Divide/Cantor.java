//UVA 11701: Cantor




import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Cantor {

	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		   Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		   while(in.hasNextFloat()){
	   float n=in.nextFloat();
	   if(n == 0 || n == 1) {
		   System.out.println("MEMBER");
	   }

	   
        else {
        	if(isCantor(n)){
     		   System.out.println("MEMBER");

        	}
        	else{
     		   System.out.println("NON-MEMBER");

        	}
        	
           
      
    }
}
}
public static boolean isCantor(float f){
	int i = 0;
	int c=0;
  
        while((f = f * 3) != 0) {
            if(i > 6){
            	break;
            }
            if(f >= 1) {
                c = (int) f;
                f = f-c;
                if(c == 1) {
                	return false;
                }
            }
            i++;
        }
    
    if(i > 6){
    	return true;
    }
    else{
    	return false;
    }


}}
	
