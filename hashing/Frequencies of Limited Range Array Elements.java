// Frequencies of Limited Range Array Elements 
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/frequency-of-array-elements/0


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args)throws Exception {
		//code
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		while(t-->0)
		{
		    int n = Integer.parseInt(br.readLine());
		    String[] s = br.readLine().split(" ");
		    
		    HashMap<Integer, Integer> map = new HashMap<>(); 
		    
		    int[] arr = new int[n];
		    
		    for(int i=0;i<n;i++)
		    {
		        int b = Integer.parseInt(s[i]);
		        if(!map.containsKey(b))
		            map.put(b,1);
		        else
		            map.put(b,map.get(b)+1);
		    }
		    
		    StringBuilder strBuilder = new StringBuilder();
            
            
		    for(int i=1;i<=n;i++)
		    {
		        
		        if(map.containsKey(i))
		            strBuilder.append(map.get(i) + " ");
		        else
		            strBuilder.append(0 + " ");
		    }
		    System.out.println(strBuilder);
		}
		
	}
}