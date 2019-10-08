// Common elements
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/common-elements/0
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
		int m = s.nextInt();
		int k = s.nextInt();
		
		Map<Integer,Integer> a = new HashMap<>();
		Map<Integer,Integer> b = new HashMap<>();
		int[] c = new int[k];
		
		for(int i=0;i<n;i++)
		    a.put(s.nextInt(),1);
		
		for(int i=0;i<m;i++)
		    b.put(s.nextInt(),1);
		
		for(int i=0;i<k;i++)
		   c[i] = s.nextInt();
		
		int flag = 0;
		for(int i=0;i<k;i++)
	    {
	        if(a.containsKey(c[i]) && b.containsKey(c[i])){
		        System.out.print(c[i] + " ");
		        a.remove(c[i]);
		        b.remove(c[i]);
		        flag=1;
    	    }
	    }
	    if(flag==0)
	        System.out.println(-1);
	    else
	        System.out.println("");
	        
		}
		
	}
}