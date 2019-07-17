So NP
13 July 2019
https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/so-np-c559f406/

/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
*/
import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class TestClass {
    
    public static boolean visited[];
    
    public static void main(String args[] ) throws Exception {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nmk = br.readLine().split(" ");
        
        int n = Integer.parseInt(nmk[0]);
        int m = Integer.parseInt(nmk[1]);
        int k = Integer.parseInt(nmk[2]);
        
        ArrayList<ArrayList<Integer>> Adj = new ArrayList<ArrayList<Integer>>();
        
        for(int i=0;i<n;i++)
            Adj.add(new ArrayList<Integer>());
            
        visited = new boolean[n];
        
        
        for(int i=0;i<m;i++)
        {
            String[] s = br.readLine().split(" ");
            int x = Integer.parseInt(s[0]);
            int y = Integer.parseInt(s[1]);
            if(x!=y)
            {
                Adj.get(x-1).add(y-1);
                Adj.get(y-1).add(x-1);
            }
        }
        
        int cc=0;
        for(int i=0;i<n;i++)
        {
            if(visited[i]==false)
            {
                cc++;
                DFS(Adj,i,n);
            }
        }
        
        if(cc>k)
            System.out.println(-1);
        else
            System.out.println(m-n+k);
        
    }
    
    public static void DFS(ArrayList<ArrayList<Integer>> Adj,int s,int n)
    {
        if(visited[s]==true)
            return;
        visited[s]=true;
        
        for(int i=0;i<Adj.get(s).size();i++)
            if(visited[Adj.get(s).get(i)]==false)
            {
                visited[Adj.get(s).get(i)]=true;
                DFS(Adj,Adj.get(s).get(i),n);
            }
    }
}
