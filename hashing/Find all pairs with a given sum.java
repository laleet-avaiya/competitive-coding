// Find all pairs with a given sum
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x/0/?ref=self



import java.util.*;
import java.lang.*;
import java.io.*;

class Node {
    int a;
    int b;
    
    Node(int a,int b){
        this.a = a;
        this.b = b;
    }
}

class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		
		while(t-->0)
		{
		    int n = s.nextInt();
		    int m = s.nextInt();
		    int k = s.nextInt();
		    
		    int a[] = new int[n];
		    int b[] = new int[m];
		    
		    Arrays.sort(a);
		    Arrays.sort(b);
		    
		    HashMap<Integer, Integer> map = new HashMap<>(); 
		    for(int i=0;i<n;i++)
		        a[i] =  s.nextInt();
		    
		    for(int i=0;i<m;i++){
		        b[i] =  s.nextInt();
		        map.put(b[i],1);
		    }
		        
		    ArrayList<Node> alist = new ArrayList<>();
		    
		    StringBuilder str = new StringBuilder(); 
		    int ans = 0;
		    for(int i=0;i<n;i++)
	        {
		        int p = a[i];
		        if(map.containsKey(k-p))
		        {
		            alist.add(new Node(p,k-p));
		            
		          //  if(ans==0)
		          //      str.append((p) + " " + (k-p) +",");
		          //  else
		          //      str.append(" " + (p) + " " + (k-p) +",");
		            ans = 1;
		        }
	        }
	        
	        Collections.sort(alist,(a1,a2)-> a1.a-a2.a);
	        
	        for(int i=0;i<alist.size();i++)
	        {
	            Node al = alist.get(i);
	            if(i==0)
	                str.append((al.a) + " " + (al.b));
	            else if(i==alist.size()-1)
	                str.append(", " + (al.a) + " " + (al.b));
	            else
	                str.append(", " + (al.a) + " " + (al.b));
	        }
	        if(ans!=0)
		        System.out.println(str);
		    else
		        System.out.println(-1);
		}
	}
}