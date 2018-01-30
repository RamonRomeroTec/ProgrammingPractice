
import java.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Main {
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		

Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));//scanner

String s= in.nextLine();
ArrayList <Integer> arr = new ArrayList<Integer>();
for(int i=0; i<s.length(); i++) {
	
	if(s.charAt(i)!='+') {
		
		arr.add(Character.getNumericValue(s.charAt(i)));

	}
	
}

Collections.sort(arr);

String nueva="";
while(!arr.isEmpty()) {
	
	if (arr.size()>1) {
		nueva=nueva+arr.get(0)+"+";
		arr.remove(0);
	}else {
		nueva=nueva+arr.get(0);
		arr.remove(0);
	}
	
}

System.out.print(nueva);




	}

}
