// Reverse words in a given string
// 12 June 2019
// https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

import java.util.*;
import java.lang.*;
import java.io.*; 


class GFG {
	public static void main (String[] args) {
        InputStreamReader r=new InputStreamReader(System.in);    
        BufferedReader br=new BufferedReader(r);            
        try
        {
        	int t = Integer.parseInt(br.readLine());
        	while(t-->0)
        	{
                String str=br.readLine();
                String[] arr = str.split("\\.");
                String sr = String.join(",", arr);

                String[] ans = new String[arr.length];
                for(int i=0;i<arr.length;i++){
                    ans[i] = arr[arr.length-1-i];
                }
                System.out.println(String.join(".",ans));
        	}
        }
        catch(IOException e)
        {
            System.out.println("Error ");
        }	

	}
}