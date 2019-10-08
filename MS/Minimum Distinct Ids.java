// Minimum Distinct Ids
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/minimum-distinct-ids/0

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
		    int[] arr = new int[n];
		    
		    Map<Integer,Integer> h = new HashMap<>();
		    
		    
		    for(int i=0;i<n;i++){
		        int a = Integer.parseInt(s[i]);
		        if(h.containsKey(a))
		            h.put(a,h.get(a)+1);
		        else
		            h.put(a,1);
		    }
		    
		    
		    int k = Integer.parseInt(br.readLine());
		    
		    ArrayList<Integer> ps = new ArrayList<>();
            for(int i:h.values())
                ps.add(i);
                
            Collections.sort(ps);
            int i=0;
            
            while(i<ps.size() && k>0)
            {
                k=k-ps.get(i);
                i++;
                if(k<0)
                    i--;
            }
                
            System.out.println(ps.size()-i);
            
            
		}
	}
}