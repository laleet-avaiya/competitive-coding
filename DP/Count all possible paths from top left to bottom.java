// Count all possible paths from top left to bottom right
// 13 June 2019
// https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right/0/?ref=self

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		InputStreamReader q = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(q);
		
		try{
		    int t = Integer.parseInt(br.readLine());
		    while(t-->0){
		        String p[] = br.readLine().split(" ");
		        int n = Integer.parseInt(p[0]);
		        int m = Integer.parseInt(p[1]);
		        
		        int G[][] = new int[m][n];
		        
		        for(int i=0;i<m;i++)
		            G[i][0]=1;
		        for(int i=0;i<n;i++)
		            G[0][i]=1;
		        G[0][0]=1;
		        
		        for(int i=1;i<m;i++)
		            for(int j=1;j<n;j++)
		                G[i][j]=(G[i-1][j] + G[i][j-1])%1000000007;
		                
		                
		        System.out.println(G[m-1][n-1]%1000000007);
		    }
		}catch(Exception e){
		    System.out.println("Laleet Practice More....");
		}
	}
}