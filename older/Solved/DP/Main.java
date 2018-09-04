//787 - Maximum Sub-sequence Product



import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

  
	    Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	    Integer n=Integer.valueOf(0);
	   while(in.hasNext()){
		    ArrayList<BigInteger> list = new ArrayList<BigInteger>();

	   while (true){
		   BigInteger n1 = in.nextBigInteger();
	    	if(n1.longValueExact()==-999999){
	    		break;
	    	}
	    		list.add(n1);
	    }
	   BigInteger Ans = BigInteger.valueOf(-999999);
       for( int i = 0 ; i < list.size() ; i++){
    	   BigInteger ret = list.get(i);
           Ans = Ans.max(ret);
           for( int j = i + 1 ; j < list.size() ; j++ ){
               ret = ret.multiply(list.get(j));
               Ans = Ans.max(ret);
           }
       }
       System.out.println(Ans);
	   }
	   
	
	}
}
       

		
	/*	Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	    Integer n=Integer.valueOf(0);
	   while(in.hasNext()){
		    ArrayList<Integer> list = new ArrayList<Integer>();

	   while (true){
		   int n1 = in.nextInt();
	    	if(n1==-999999){
	    		break;
	    	}
	    		list.add(n1);
	   }
	   
	   int sum=1,mxV=-999999;

       for(int j=0;j<list.size();j++)
       {
           sum=1;
           for(int k=j;k<list.size();k++)
           {
               sum=sum*list.get(k);
           }
           if(mxV<sum)mxV=sum;
       }
       System.out.println(mxV);
*/

 