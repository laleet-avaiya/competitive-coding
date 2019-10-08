// Remove character
// 12 June 2019
// https://practice.geeksforgeeks.org/problems/remove-character/0

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		try{
    		InputStreamReader p = new InputStreamReader(System.in);
    		BufferedReader br = new BufferedReader(p);
    		
    		int t = Integer.parseInt(br.readLine());
    		while(t-->0){
    		    String s1 = br.readLine();
    		    String s2 = br.readLine();

    		  int[] ch = new int[256];
    		  for(int i=0;i<s2.length();i++)
    		      ch[(int)s2.charAt(i)] = 1;
    		  
    		  int j=0;
    		  for(int i=0;i<s1.length();i++)
    		        if( ch[(int)s1.charAt(i)] != 1)
    		            System.out.print(s1.charAt(i));
    		  System.out.println();
    		}
		}catch(Exception e){
		    System.out.println(e);
		}
	}
}