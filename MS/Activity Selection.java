// Activity Selection
// 18 July 2019
// https://practice.geeksforgeeks.org/problems/activity-selection/0
// /*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class Pair{
    int start;
    int end;
    Pair(int a,int b)
    {
        this.start = a;
        this.end = b;
    }
}

class GFG {
	public static void main (String[] args)throws Exception {
		//code
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		

		int t = Integer.parseInt(br.readLine());
		
		while(t-->0)
		{
		    int n = Integer.parseInt(br.readLine());
		    
		    ArrayList<Pair> alist = new ArrayList<>();
		    
		    String[] ss = br.readLine().split(" ");
		    String[] se = br.readLine().split(" ");
		    
		    for(int i=0;i<n;i++)
		        alist.add(new Pair(Integer.parseInt(ss[i]),Integer.parseInt(se[i])));
		  
		    Collections.sort(alist,(o1,o2)-> {
		            return (o1.end-o2.end);
		    });
	        
		    Pair prev = new Pair(alist.get(0).start,alist.get(0).end);
	        alist.remove(0);
		  
		    int ans = 0;
            for(Pair a: alist)
            {
                if(a.start>=prev.end)
                {
                    ans++;
                    prev = a;
                }
            }
            
            alist.clear();
		    System.out.println(ans);
		}
		
	}
}