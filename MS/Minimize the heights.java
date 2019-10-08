// Minimize the heights
// 19 July 2019
// https://practice.geeksforgeeks.org/problems/minimize-the-heights/0/?ref=self


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;


/*

1. return largest - smallest , if their difference is less than k, otherwise see below steps
2. calculate average = (smallest + largest ) /2
3. increase the values below average by k
4. decrease values above average by k
5. find the smallest and largest values again and return their absolute difference.

*/

class GFG {
	public static void main (String[] args) {
		//code
		
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t-->0)
		{
		    int k = s.nextInt();
		    int n = s.nextInt();
		    int[] arr = new int[n];
		    
		    
		    for(int i=0;i<n;i++)
		        arr[i] = s.nextInt();
		    
		    
	        Arrays.sort(arr);
		    int avg = (arr[n-1]+arr[0])/2;
		    
		    if(arr[n-1]-arr[0] < k )
		    {
		        System.out.println(arr[n-1]-arr[0]);
		    }
		    else
		    {
    		     for(int i=0;i<n;i++)
    		    {
    		        if(arr[i]<avg)
    		            arr[i] = arr[i] + k;
    		        else
    		            arr[i] = arr[i] - k;
    		    }
    		    Arrays.sort(arr);
    		    System.out.println(arr[n-1]-arr[0]);
		    }
		}
	}
}