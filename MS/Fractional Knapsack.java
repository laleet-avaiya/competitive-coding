// Fractional Knapsack
// 18 July 2019
// https://practice.geeksforgeeks.org/problems/fractional-knapsack/0


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class Pair{
    
    double val;
    double weight;
    
    Pair(double a,double b){
        this.val = a;
        this.weight = b;
    }
}

class GFG {
    
    public static double knapSack(ArrayList<Pair> vw, int n,int W)
    {
        double ans = 0;
        for(int i=0;i<n;i++)
        {
            if(vw.get(i).weight<=W)
            {
                ans += vw.get(i).val;
                W -= vw.get(i).weight;
            }
            else
            {   
                double fraction = ((double)W/(double)vw.get(i).weight); 
                ans += (vw.get(i).val*fraction); 
                break; 
            }
        }
        
        return ans;
        
    }
    
	public static void main (String[] args)throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine());
		
		while(t-->0)
		{
		    String[] nW = br.readLine().split(" ");
		    int n = Integer.parseInt(nW[0]);
		    int W = Integer.parseInt(nW[1]);
            
            String[] p = br.readLine().split(" ");
            ArrayList<Pair> alist = new ArrayList<>();
            
		    for(int i=0;i<n+n;i=i+2)
		        alist.add(new Pair(Integer.parseInt(p[i]),Integer.parseInt(p[i+1])));
		        
		    Collections.sort(alist,(o1,o2) -> { 
		        Double ratio1 = new Double(o1.val/o1.weight);
		        Double ratio2 = new Double(o2.val/o2.weight);
		        return ratio2.compareTo(ratio1);
		    });
            
            System.out.format("%.2f", knapSack(alist,n,W));
            System.out.println("");
		}
	}
}