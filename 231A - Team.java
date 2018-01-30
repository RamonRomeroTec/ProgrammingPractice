

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

		

Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));//scanner

int casos=in.nextInt();
int realizable=0;
for (int i=0; i<casos; i++) {
	int suma=0;

	for (int j=0; j<3; j++) {
		int ans=in.nextInt();
		
		suma=suma+ans;
		
		

	}
	
	if (suma>=2) {
		
		realizable++;
	}

	
}

System.out.print( realizable);

	}

}
