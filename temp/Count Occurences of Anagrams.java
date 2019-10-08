/*
    Todo Count Occurences of Anagrams
    Todo 04 Aug. 2018
    Todo https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams/0
*/

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = Integer.parseInt(s.next());
		while(t-->0)
		{
		    String str = s.next();
		    String pat = s.next();
		    
		    int n = str.length();
		    int m = pat.length();
		    int count = 0;
		    
		    int[] pat_fre = new int[256];
		    
		    for(int i=0;i<m;i++){
		        pat_fre[pat.charAt(i)]++;
		    }
		    
		    for(int i=0;i<n-m+1;i++)
		    {
		        int[] curr_wind_size_m_freq = new int[256];
		        
		        // Store Freq of window size m in array 
		        for(int j=i;j<i+m;j++)
		            curr_wind_size_m_freq[str.charAt(j)]++;
		          
		        
		        //  compare two Array if same count ++
		        boolean match = true;
		        for(int k=0;k<256;k++)
		        {
		            if(curr_wind_size_m_freq[k]!=pat_fre[k])
		                match=false;
		        }
		        
		        if(match==true)
		            count++;
		    }
		    System.out.println(count);
		}
	}
}