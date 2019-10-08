// Equal 0, 1 and 2 
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/equal-0-1-and-2/0

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
        Scanner s1 = new Scanner(System.in);
        int n = s1.nextInt();
        int arr[]=new int[3];
        
        for(int i=0;i<n;i++)
        { 
            int count=0; 
            String s=s1.next();
            for(int k=0; k<s.length();k++)
            {
                for(int j=k+2;j<s.length();j=j+3)
                {
                    String sub=s.substring(k,j+1);
                    for(int m=0;m<sub.length();m++)
                    {
                        arr[Character.getNumericValue(sub.charAt(m))]++;
                    }
                    if(arr[0]==arr[1] && arr[0]==arr[2])
                        count++;
                    arr[0]=arr[1]=arr[2]=0;
                }
            }
            System.out.println(count);
        }
	}
}