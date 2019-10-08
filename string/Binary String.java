// Binary String 
// 12 June 2019
// https://practice.geeksforgeeks.org/problems/binary-string/0
// https://practice.geeksforgeeks.org/problems/binary-string/1

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
	            int n = Integer.parseInt(br.readLine());
	            String s = br.readLine();
	            int[] count = new int[n];
	            int prev = 0;
	            int ans=0;
	            
	            for(int i=n-1;i>=0;i--)
	            {
	                if(s.charAt(i)=='1'){
	                    count[i]= prev;
	                    prev = 1 + count[i];
	                    ans+=count[i];
	                }
	            }
	            System.out.println(ans);    
	            
	        }
	        
	    }catch(Exception e){
	        System.out.println("error");
	    }
	}
}