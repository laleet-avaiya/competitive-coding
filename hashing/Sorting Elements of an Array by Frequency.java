// Sorting Elements of an Array by Frequency
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
// /*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code4
		Scanner s = new Scanner(System.in);
		int t = s.nextInt();
		while(t-->0){
		    int n = s.nextInt();
		    int[] arr = new int[n];
		    int a;
		  //  Hashtable<Integer,Integer> h = new Hashtable<>();
		    Map<Integer,Integer> h=new HashMap<>();
		    
		    
		    
		    for(int i=0;i<n;i++)
		    {
		        arr[i] = s.nextInt();
		        if(h.containsKey(arr[i]))
		        {
		            h.put(arr[i],h.get(arr[i])+1);
		        }
		        else{
		            h.put(arr[i],1);
		        }
		    }
		    
		    
	      int max=0;
	      for(int i=0;i<n-1;i++)
	      {
              for(int j=i+1;j<n;j++)
              {
                if(h.get(arr[i])<h.get(arr[j]) ||(h.get(arr[i])==h.get(arr[j]) && arr[i]>arr[j]))
                {
                    int temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
                   
              }
	      }
	      
	      for(int i=0;i<n;i++)
	            System.out.print(arr[i]+" ");
		  System.out.println(" ");
		    
		}
	}
}