// Smallest Positive missing number 
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0/?ref=self
// /*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		while(t-->0){
		    int n = s.nextInt();
		    int[] arr = new int[n];
		    
		    Map<Integer,Integer> h = new HashMap<>();
		    for(int i=0;i<n;i++)
            {		        
                arr[i] = s.nextInt();
                h.put(arr[i],1);
            }
            
            for(int i=1;i<1000000;i++)
            {		        
                if(h.containsKey(i)==false)
                {
                    System.out.println(i);
                    break;
                }
            }
		    
		}
		
	}
}