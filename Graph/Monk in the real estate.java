// Monk in the real estate
// 16 July 2019

// https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/monk-in-the-real-estate/

import java.util.*;

class TestClass {
    public static void main(String args[] ) throws Exception {
        
        // Write your code here
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        
        while(t-->0)
        {
            int e = s.nextInt();
            HashMap<Integer,Integer> h = new HashMap<>();
            
            for(int i=0;i<2*e;i++)
                h.put(s.nextInt(),1);
    
            System.out.println(h.size());
        }

    }
}
