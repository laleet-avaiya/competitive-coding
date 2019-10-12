// Reverse Level Order Traversal 
// 09 Oct. 2019
// https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1/?ref=self

class Temp{
    Node node;
    int level;
    
    Temp(Node n,int l){
        this.node = n;
        this.level = l;
    }
}
class GfG
{
	void reversePrint(Node node) 
    {
        Queue<Temp> q=new LinkedList<>();
        Stack<List<Integer>> st=new Stack<>();
        List<Integer> lst = new ArrayList<Integer>();
        int prev_level = 1;
        
        q.add(new Temp(node,1));
        while(!q.isEmpty())
        {
            Temp a = q.remove();
            
            Node temp = a.node;
            int level = a.level;
            
            if(prev_level==level)
            {
                lst.add(temp.data);
            }
            else
            {
                st.push(lst);
                lst = null;
                lst = new ArrayList<Integer>();
                lst.add(temp.data);
                prev_level = level;
            }
            
             
            if(temp.left!=null)
                q.add(new Temp(temp.left,level+1));
                
            if(temp.right!=null)
                q.add(new Temp(temp.right,level+1));
        }
        
        st.push(lst);
        
            
        while(!st.isEmpty())
        {
            List<Integer> p = st.pop();
            for(int i=0;i<p.size();i++)
            {
                System.out.print(p.get(i)+" ");    
            }
        }
            
    }
} 