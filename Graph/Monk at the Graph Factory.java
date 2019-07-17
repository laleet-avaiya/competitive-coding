Monk at the Graph Factory 
13 July 2019

// https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-at-the-graph-factory/

/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.InputStreamReader;

//import for Scanner and other utility classes
*/
import java.util.*;
import java.io.*;

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class TestClass {
    public static void main(String args[] ) throws Exception {
        
        // Write your code here
        Scanner s = new Scanner(System.in);
        
        int n = s.nextInt();
        int ans=0;
        
        for(int i=0;i<n;i++)
            ans+=s.nextInt();
        
        if(ans==((n-1)*2))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}
