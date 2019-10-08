// Minimum changes to make all substrings distinct 
// https://practice.geeksforgeeks.org/problems/minimum-changes-to-make-all-substrings-distinct/0

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
		        String s = br.readLine();
		        int arr[] = new int[26];
		        int ans=0;
		        for(int i=0;i<s.length();i++)
		            arr[(int)s.charAt(i)-97]++;
		        
		        for(int i=0;i<26;i++)
		            if(arr[i]>1)
		                ans = ans + arr[i]-1;
		        
		        System.out.println(ans);
		    }
		}catch(Exception w){
		    System.out.println("Practice More Laleet....");
		}
	}
}