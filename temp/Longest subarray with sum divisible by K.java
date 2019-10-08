/*
Todo : Longest subarray with sum divisible by K 
Todo : 05 Aug. 2019
Todo : https://practice.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k/0
*/

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
	public static void main (String[] args)
	 {
	 Scanner sc=new Scanner(System.in);
	 int tc=sc.nextInt();
	 while(tc-->0)
	 {
	     
	     int n=sc.nextInt();
	     int k=sc.nextInt();
	     int max=0,curr_sum=0;
	     int arr[]=new int[n];
	     int sum[]=new int[n];
	     
	     for(int i=0;i<n;i++)
	     {
	         int a=sc.nextInt();
	         curr_sum=curr_sum+a;
	         sum[i]=((curr_sum % k) + k) % k; 
	     }
	     
	     HashMap<Integer,Integer> m = new HashMap<Integer,Integer>();
	     for(int j=0;j<n;j++)
	     {
	        if(sum[j]==0)
	            max=Math.max(max,j+1);
	        else if (m.containsKey(sum[j]) == false) 
                m.put(sum[j] , j);
            else
                // if true, then update 'max' 
                if (max < (j - m.get(sum[j]))) 
                    max = j - m.get(sum[j]);   
	     }
	     System.out.println(max);
	 }
	 }
}