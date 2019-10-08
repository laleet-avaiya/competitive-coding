// Common Subsequence 
// 13 June 2019
// https://practice.geeksforgeeks.org/problems/common-subsequence/0

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		InputStreamReader p = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(p);
		
		try{
		    int t = Integer.parseInt(br.readLine());
		    while(t-->0){
		        String[] str = br.readLine().split(" ");
		        
		        String a = str[0];
		        String b = str[1];
		        int[] temp =new int[26];
		        
		        int ans =0;
		        for(int i=0;i<a.length();i++)
		            temp[(int)a.charAt(i)-65]++;
		        
		        for(int i=0;i<b.length();i++)
		            if(temp[(int)b.charAt(i)-65]!=0){
		                ans = 1;
		                break;
		            }
		            
		        System.out.println(ans);
		    }
		    
		    
		}catch(Exception e){
		    System.out.println("Practice More Laleet....");
		}
	}
}