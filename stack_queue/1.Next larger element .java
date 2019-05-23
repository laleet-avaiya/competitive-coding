

// Next larger element 
// https://practice.geeksforgeeks.org/problems/next-larger-element/0


import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t-->0){
		    int n = s.nextInt();
		    long[] arr = new long[n];
		    long[] ans = new long[n];
		    
		    for(int i=0;i<n;i++){
		        arr[i]=s.nextLong();
		    }
		    
		    long last_max = arr[n-1];
		    ans[n-1]=-1;
		    
		    for (int i=n-2;i>=0;i--){
		        
		        if(arr[i]<arr[i+1]){
		            ans[i]=arr[i+1];
		            if(arr[i+1] > last_max){
		                last_max = arr[i+1];
		            }
		        }
		        else if(arr[i]<last_max){
		            
		            int j=i;
		            while(arr[j] != last_max){
		                if(j>=n){
		                    ans[i]=-1;
		                    last_max=arr[i];
		                    break;
		                }
		                if(arr[j]>arr[i]){
		                    ans[i]=arr[j];
		                    break;
		                }
		                j++;
		            }
		            
		            if(arr[j] == last_max){
		                ans[i]=last_max;
		            }
		            
		        }else{
		            ans[i]=-1;
		        }
		        
		    }
		    
		    for(int i=0;i<n;i++)
		    {
		        System.out.print(ans[i] +" ");
		    }
		    System.out.println("");
		}
	}
}

// Stack 

// if stack is Empty : -1
// pop until not found > present Number => if found the print it.


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner ss = new Scanner(System.in);
		
		int t = ss.nextInt();
		
		while(t-->0){
		    int n = ss.nextInt();
		    long[] arr = new long[n];
		    long[] ans = new long[n];
		    
		    for(int i=0;i<n;i++){
		        arr[i]=ss.nextLong();
		    }
		    
		    Stack<Long> s = new Stack<Long>();
		    
		    for(int i=n-1;i>=0;i--){
		        
		       
		        while(!s.isEmpty()){
		            if(s.peek()<arr[i]){
		                s.pop();
		            }else{
		                 ans[i]=s.peek();
		                 s.push(arr[i]);
		                 break;
		            }
		        }
		        if(s.isEmpty()){
		            ans[i]=-1;
		            s.push(arr[i]);
		        }
		      
		    }
		   
		    for(int i=0;i<n;i++)
		    {
		        System.out.print(ans[i] +" ");
		    }
		    System.out.println("");
		}
	}
}