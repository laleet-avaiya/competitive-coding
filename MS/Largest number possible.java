// Largest number possible 
// 19 July 2019
// https://practice.geeksforgeeks.org/problems/largest-number-possible/0/?ref=self


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t-->0)
		{
		    int n = s.nextInt();
		    int sum = s.nextInt();
		    
		    StringBuilder ans = new StringBuilder();
	        if(sum!=0)
    		    for(int i=0;i<n;i++)
    		    {
    		        if(sum>9)
    		        {
    		            ans.append(9);
    		            sum = sum -9;
    		        }
    		        else if(sum==0)
    		            ans.append(0);
    		        else
    		        {
    		            ans.append(sum);
    		            sum = 0;
    		        }
    		    }
    		else
    		    sum = -1;
		    
		    if(sum==0)
		        System.out.println(ans);
		    else
		        System.out.println(-1);
		    
		}
	}
}