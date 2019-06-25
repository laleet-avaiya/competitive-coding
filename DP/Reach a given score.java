// Reach a given score
// 14 June 2019
// https://practice.geeksforgeeks.org/problems/reach-a-given-score/0

/*package whatever //do not write package name here */

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
		    
		    int a[] = new int[n+1];
		    a[0]=1;
		    
		    for(int i=3;i<=n;i++)
		        a[i] += a[i-3];
		        
		    for(int i=5;i<=n;i++)
		        a[i] += a[i-5];
		        
   
		    for(int i=10;i<=n;i++)
		        a[i] += a[i-10];
		    
		    System.out.println(a[n]);
		}
	}
}