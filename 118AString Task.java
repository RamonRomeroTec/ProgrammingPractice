

import java.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		

HashSet<Character> hs = new HashSet<Character>();

hs.add('a');
hs.add('e');
hs.add('i');
hs.add('o');
hs.add('u');

hs.add('y');


Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));//scanner
Stack <Character> st = new Stack<Character>();
String s=in.nextLine();
s=s.toLowerCase();
for (int i=s.length()-1; i>=0; i--) {
	
	if( hs.contains(s.charAt(i)) ) {
		//es vocal
		//System.out.print("-");
	}else {
		
		st.add(s.charAt(i));
		st.add('.');
		//System.out.print("*");


		
		
		
	}
	
	

}
String nw = "";

while(!st.empty()) {
	nw=nw.concat(st.pop().toString());
		
}


		    
		  System.out.print(nw);
		   
		   

	}

}
