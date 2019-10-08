// Anagram Palindrome 
// 12 June 2019
// https://practice.geeksforgeeks.org/problems/anagram-palindrome/0

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		InputStreamReader p = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(p);
		
		try{
		    int t  = Integer.parseInt(br.readLine());
		    while(t-->0)
		    {
		    String s = br.readLine();
		    int n = s.length();
		    int count[] = new int[26];
		    
		    for(int i=0;i<n;i++)
		        count[(int)s.charAt(i)-97]++;    
		    
		    String ans = "Yes";
		    
		    if(n%2==0)
		    {
                for(int i=0;i<26;i++)
                if(count[i]%2!=0)
                {
                    ans ="No";
                    break;
                }
		    }
		    else
		    {
		        int temp = 0;
		        for(int i=0;i<26;i++)
                if(count[i]%2!=0)
                {
                    temp++;
                    if(temp>1)
                    {
                        ans ="No";
                        break;
                    }
                }
	            
		    }
		    System.out.println(ans);
    		}
    		}
    		catch(Exception e ){
    		    System.out.println(e);
    		}
		
	}
}