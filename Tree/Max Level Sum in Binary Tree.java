// Max Level Sum in Binary Tree 
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1


class NodeLevel {
        public Node node;
        public int level;
        
        NodeLevel(Node p,int l){
            this.node = p;
            this.level = l;
        }
    }
    
class GfG
{
    
	public static int maxLevelSum(Node root)
    {
        //add code here.
        
        int currentlevel=-1;
        int maxi=-9999999;
        int total=0;
        
        Queue<NodeLevel> q = new LinkedList<>();
        q.add(new NodeLevel(root,0));
        while(!q.isEmpty()){
            
            NodeLevel s = q.remove();
            
            Node p = s.node;        // Node
            int temp = s.level;     // Level
            if(currentlevel!=temp)
            {
                if(total>maxi)
                    maxi=total;
                currentlevel = temp;
                total=0;
            }
            
            total+=p.data;
            
            if(p.left!=null){
                q.add(new NodeLevel(p.left,temp+1));
            }
            
            if(p.right!=null){
                q.add(new NodeLevel(p.right,temp+1));
            }
        }
        
        if(total>maxi) return total;
        return maxi;
    }
}