// Level order traversal Line by Line 
// 18 July 2019
// https://practice.geeksforgeeks.org/problems/level-order-traversal-line-by-line/1

class Temp{
    Node node;
    int level;
    
    Temp(Node n,int l)
    {
        this.node = n;
        this.level =l;
    }
}
class Level_Order_Traverse
{
    static void levelOrder(Node node) 
    {
        // Your code here
        
        Queue<Temp> q = new LinkedList<>();
        
        q.add(new Temp(node,0));
        int prevlevel=0;
        while(q.size()>0)
        {
            Temp qs = q.poll();
            Node p = qs.node;
            if(prevlevel!=qs.level)
            {
                prevlevel = qs.level;
                System.out.print("$" +" ");
            }
            System.out.print(p.data +" ");
            
            if(p.left!=null)
                q.add(new Temp(p.left,qs.level+1));
                
            if(p.right!=null)
                q.add(new Temp(p.right,qs.level+1));
        }
        System.out.print("$");
    }
}