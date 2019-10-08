// Keypad typing
// 12 June 2019
// https://practice.geeksforgeeks.org/problems/keypad-typing/0


import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		int[] ord = {2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9};
		
		InputStreamReader p = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(p);
		
		try{
    		int t = Integer.parseInt(br.readLine());
    		while(t-->0){
    		    String s = br.readLine();
    		    
    		    for(int i=0;i<s.length();i++)
    		        System.out.print(ord[(int)s.charAt(i)-97]);
    		    System.out.println();
    		}
		}
		catch(Exception e){
		    System.out.println("error");
		}
	}
}