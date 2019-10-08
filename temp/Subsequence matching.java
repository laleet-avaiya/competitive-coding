/* 
    Todo Subsequence matching
    Todo 04 Aug. 2019
    Todo https://practice.geeksforgeeks.org/problems/subsequence-matching/0
*/

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {

    public static boolean SolveProblem(String p)
    {
        p = p.replaceAll("RYY","_");
        p = p.replaceAll("RY","_");
        p = p.replaceAll("R","_");
        int n = p.length();

        for(int i=0;i<n;i++)
            if(p.charAt(i)!='_')
                return false;
        return true;
    }

	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		int t = Integer.parseInt(s.next());
    while(t-->0)
    {
        String input = s.next();
        if(SolveProblem(input))
            System.out.println("YES");
        else
            System.out.println("NO");
    }
	}
}
