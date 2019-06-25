// Positive and negative elements
// 13 June 2019
// https://practice.geeksforgeeks.org/problems/positive-and-negative-elements/0/?ref=self


import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		
		InputStreamReader p = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(p);
		
		try{
		    int t = Integer.parseInt(br.readLine());
		    while(t-->0){
		        int n = Integer.parseInt(br.readLine());
		        String[] arr =(br.readLine().split(" "));
		      //  int[] s = new int[n];
		        
		        int[] po = new int[n/2];
		        int[] ne = new int[n/2];
		        
		        
		        int jj=0;
		        int temp=0;
                int j=0,k=0;   
                
		        for(String i:arr){
		            temp = (Integer.parseInt(i));
		            
		            if(temp<0){
		                ne[j] = temp;
		                j++;
		            }
		            else{
		                po[k] = temp;
		                k++;
		            }
		            jj++;
		        }
		        
		        
		         for(int i=0;i<n/2;i++){
		             System.out.print(po[i]+" ");
		             System.out.print(ne[i] + " ");
		            
		            
		        }
		        System.out.println("");
		    }
		    
		    
		}catch(Exception e){
		    System.out.println("Laleet Practice More...");
		}
		
		
	}
}