// Knapsack with Duplicate Items 
// 19 July 2019
// https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items/0/?ref=self

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    // Returns the maximum value with knapsack of W capacity 
    private static int unboundedKnapsack(int W, int n,int[] val, int[] wt) 
    { 
        // dp[i] is going to store maximum value 
        // with knapsack capacity i. 
        int dp[] = new int[W + 1]; 
          
        // Fill dp[] using above recursive formula 
        for(int i = 0; i <= W; i++)
            for(int j = 0; j < n; j++) 
                if(wt[j] <= i)
                    dp[i] = Math.max(dp[i], dp[i - wt[j]] + val[j]); 
            
        return dp[W]; 
    } 
    
    
	public static void main (String[] args) {
		//code
		
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t-->0)
		{
		    int n = s.nextInt();
		    int W = s.nextInt();
		    
		    int[] val = new int[n];
		    int[] wt = new int[n];
		    
		    for(int i =0;i<n;i++)
		        val[i] = s.nextInt();
		        
		    for(int i =0;i<n;i++)
		        wt[i] = s.nextInt();
		        
		    System.out.println(unboundedKnapsack(W,n,val,wt));
		}
	}
}