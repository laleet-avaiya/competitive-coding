/*
Todo Longest Even Length Substring
Todo 04 Aug. 2019
Todo https://practice.geeksforgeeks.org/problems/longest-even-length-substring/0
*/


import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    static int findLength(String str) 
    { 
        int n = str.length(); 
        int maxlen = 0; // Initialize result 
      
        // Choose starting point of every  
        // substring 
        for (int i = 0; i < n; i++) 
        { 
            // Choose ending point of even  
            // length substring 
            for (int j = i + 1; j < n; j += 2) 
            {    
                // Find length of current substr 
                int length = j - i + 1; 
      
                // Calculate left & right sums 
                // for current substr 
                int leftsum = 0, rightsum = 0; 
                for (int k = 0; k < length/2; k++) 
                { 
                    leftsum += (str.charAt(i + k) - '0'); 
                    rightsum += (str.charAt(i + k + length/2) - '0'); 
                } 
      
                // Update result if needed 
                if (leftsum == rightsum && maxlen < length) 
                        maxlen = length; 
            } 
        } 
        return maxlen; 
    } 


	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = Integer.parseInt(s.next());
		while(t-->0)
		{
		    String n = s.next();
		    System.out.println(findLength(n));
		}
	}
}