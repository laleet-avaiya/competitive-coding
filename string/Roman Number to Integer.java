// Roman Number to Integer
// 13 June 2019
// https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0



import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    public static int value(char r) 
    { 
        if (r == 'I') 
            return 1; 
        if (r == 'V') 
            return 5; 
        if (r == 'X') 
            return 10; 
        if (r == 'L') 
            return 50; 
        if (r == 'C') 
            return 100; 
        if (r == 'D') 
            return 500; 
        if (r == 'M') 
            return 1000; 
        return -1; 
    } 
    
	public static void main (String[] args) {
		//code
		InputStreamReader p = new InputStreamReader(System.in);
		BufferedReader br = new BufferedReader(p);
		
		
		
		try{
		    int t = Integer.parseInt(br.readLine());
		    while(t-->0){
		        String str= br.readLine();
		        int res = 0; 
		        
		        
		         for (int i=0; i<str.length(); i++) 
                { 
                
                    int s1 = value(str.charAt(i)); 
                
                 
                    if (i+1 <str.length()) 
                    { 
                        int s2 = value(str.charAt(i+1)); 
                
                        
                        if (s1 >= s2) 
                        { 
                            
                            res = res + s1; 
                        } 
                        else
                        { 
                            res = res + s2 - s1; 
                            i++;
                          
                        } 
                    } 
                    else
                    { 
                        res = res + s1; 
                        i++; 
                    } 
                } 
                System.out.println(res); 
		        
		    }
		    
		}catch(Exception e){
		    System.out.println("Error" + e );
		}
	}
}