// Odd to Even 
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/odd-to-even/0

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    public static String oddeven(String str){
        int len = str.length();
        int max = Integer.MIN_VALUE;
        
        for(int i = 0 ; i < len - 1 ; i++){
             int ch = str.charAt(i);
           
             if(ch % 2 == 0 ){
              
              char[] str1 = str.toCharArray();
              str1[i] = str.charAt(len-1);
              str1[len-1] = str.charAt(i);
              
              max = Math.max(Integer.parseInt(String.valueOf(str1)) , max);
          }
      }
      
      if(max == Integer.MIN_VALUE)
          return str;
      
      else {
          return String.valueOf(max);
      }
      
    }
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T-- > 0){
		    String str = sc.next();
		    GFG gf = new GFG();
		    String result = gf.oddeven(str);
		    System.out.println(result);
		}
	}
}