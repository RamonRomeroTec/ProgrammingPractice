package divideConquista;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	
	  
	  public static String generate(int pos){ 
		  String list="";



	int i,j,c=0;
	for(i=1;c<pos;i++)
	{
	for(j=1;j<=i&&c<pos;j++)
	{
		c++;
		String num= Integer.toString(j);
		list=list+num;


	
	
	}

	}
	return list;
	}
	  
	  
	  
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		 Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	   int n=in.nextInt();
   	int [] arr = new int[n];

	   for (int c=0; c<n; c++){

		  arr[c]=in.nextInt();



		 
		   
	   }
	   Arrays.sort(arr);
	   String gen=generate(arr[arr.length-1]);
	   for (int c=0; c<n; c++){

			  System.out.println(gen.charAt(arr[c]-1));



			 
			   
		   }
	   
	}
	   }
	  
	   

			//11212312341234512345/6123456712/345678123456789123456789101234567891011
		  	//112123123412345123456123456712345678123456789123456789101234567891011

	
	
	
	

/**
 * 
 * package divideConquista;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	
	  
	  public static ArrayList<Integer> generate(int pos){ 
		  ArrayList<Integer> list = new ArrayList<Integer>();


	int i,j,c=0;
	for(i=1;c<pos;i++)
	{
	for(j=1;j<=i&&c<pos;j++)
	{
		c++;
		list.add(j);
	
	
	}
	}
	
	return list;
	}
	  
	  
	  
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		 Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	   int n=in.nextInt();

	   for (int c=0; c<n; c++){

		  int r=in.nextInt();
			  ArrayList<Integer> list = generate(r);


		 
		   
	   }
	   Arrays.sort(locs);
	   int max = locs[locs.length - 1];
	   
	   
		  ArrayList<Integer> list = generate(max);
	  
		  for (int c=0; c<n; c++){

			   System.out.println(list.get(locs[c]-1));

			 
			   
		   }
	   

			//112123123412345123456123456712345678123456789123456789101234567891011
		  	//112123123412345123456123456712345678123456789123456789101234567891011

	}
	
	
	
}

 * 
 * */
 