// Number of Coins
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/number-of-coins/0

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args)throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		while(t-->0)
		{
		    String[] nc = br.readLine().split(" ");
		    
		    int n = Integer.parseInt(nc[0]);
		    int c = Integer.parseInt(nc[1]);
		    
		    int[] arr = new int[c];
		    int[] ans = new int[n+1];
		    
		    String[] vc = br.readLine().split(" ");
		    
		    for(int i=0;i<c;i++)
		        arr[i] = Integer.parseInt(vc[i]);
		        
		    for(int i=1;i<n+1;i++)
		        ans[i] = 99999;
		    
		    ans[0] = 0;
		  
		    for(int i=0;i<c;i++)
		        for(int j=arr[i];j<n+1;j++)
		            ans[j] = Math.min(ans[j],ans[j-arr[i]]+1);
		        
		    if(ans[n]==99999)
		        System.out.println(-1);
		    else
		        System.out.println(ans[n]);
		    
		}
	}
}