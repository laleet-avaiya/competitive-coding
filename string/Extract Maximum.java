// Extract Maximum 
// https://practice.geeksforgeeks.org/problems/extract-maximum/0
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;


class GFG {
    public static Scanner sc = new Scanner(System.in);
	public static void main (String[] args) {
		int T = sc.nextInt();
		
		while(T-- > 0) {
		    String str = sc.next();
		    int n =str.length();
		    int finalans = 0;
		    int ans=0;
		    int size=0;
		    for(int i=n-1;i>=0;i--) {
		        if((int)str.charAt(i)>95 && (int)str.charAt(i) <124 ){
		            if(ans>finalans)
		                finalans = ans;
		            size=0;
		            ans=0;
		            continue;
		        }else{
		            ans += Character.getNumericValue(str.charAt(i))*Math.pow(10,size++);
		        }
		        
		  }
		  if(ans>finalans)
		    finalans = ans;
		  System.out.println(finalans);
		}
	}
}