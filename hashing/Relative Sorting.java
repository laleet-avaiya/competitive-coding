// Relative Sorting 
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/relative-sorting/0


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
	        int m = s.nextInt();
	        
	        int[] A = new int[n];
	        int[] B = new int[m];
	        int[] H = new int[1000000];
	        for(int i=0;i<n;i++)
            {   
                A[i] = s.nextInt();
                H[A[i]]++;
            }
                
            for(int i=0;i<m;i++)
            {
               B[i] = s.nextInt();
                while(H[B[i]]-->0)
                {
                    System.out.print(B[i] + " ");
                }
            }
            
            Arrays.sort(A);
            
            for(int i=0;i<n;i++)
                while(H[A[i]]-->0)
                    System.out.print(A[i] + " ");
            
            System.out.println("");
	    }
	}
}