// Rod Cutting 
// 19 July 2019
// https://practice.geeksforgeeks.org/problems/rod-cutting/0/?ref=self

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt(),n;
		for(int tc=0;tc<t;tc++){
		    n=sc.nextInt();
		    int[] a=new int[n+1];
		    for(int i=1;i<n+1;i++)
		        a[i]=sc.nextInt();
		        
		    int[] b=new int[n+1];
		    b[0]=0;
		    for(int i=1;i<n+1;i++){
		        int max=Integer.MIN_VALUE;
		        for(int j=i;j>-1;j--){
		            if(a[j]+b[i-j]>max)
		                max=a[j]+b[i-j];
		        }
		        b[i]=max;
		    }
		        System.out.println(b[n]);
		}
	}
}