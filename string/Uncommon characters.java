// Uncommon characters
// https://practice.geeksforgeeks.org/problems/uncommon-characters/0/?ref=self

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		s.nextLine();
		
		while(t-->0){
		    String s1 = s.nextLine();
		    String s2 = s.nextLine();
		    
		    int temp[] = new int[255];
		      int temp1[] = new int[255];
		    
		    for(int i=0;i<s1.length();i++)
		        temp[(int)s1.charAt(i)]=1;
		        
		    for(int i=0;i<s2.length();i++)
		       temp1[(int)s2.charAt(i)]=1;
		    
		    for(int i=96;i<124;i++)
		       { 
		           if(temp[i]!=temp1[i])
		            System.out.print((char)(i));
		           
		       }
		  System.out.println(" ");
		}
		
	}
}