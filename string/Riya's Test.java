Riya's Test
https://practice.geeksforgeeks.org/problems/riyas-test/0/?ref=self


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
		        String s = br.readLine();
		        int n = s.length();
		        int left[] = new int[255];
		        int right[] = new int[255];
		        
		        if(n%2==0){
		            for(int i=0;i<n/2;i++){
		                left[(int)s.charAt(i)]++;
		                right[(int)s.charAt(n/2 + i)]++;
		            }
		        }else{
		            for(int i=0;i<n/2;i++){
		                left[(int)s.charAt(i)]++;
		                right[(int)s.charAt(n/2 + 1+i)]++;
		            }
		        }
		        
		        String ans = "YES";
		        for(int i=0;i<255;i++){
		            if(left[i]!=right[i]){
		                ans="NO";
		                break;
		            }
		                
		        }
		        
		        System.out.println(ans);
		    }
		}catch(Exception e){
		    System.out.println("Laleet Practice More.....");
        }
		
	}
}