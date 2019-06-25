// Connect Nodes at Same Level 
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1/?ref=self
class GfG
{
    Node connect(Node root)
    {
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            Node node = q.remove();
            if(node.left!=null)
            {   
                q.add(node.left);
                node.left.nextRight = node.right;
            }
            if(node.right!=null)
            {   
                q.add(node.right);
                node.right.nextRight = (node.nextRight!=null)?node.nextRight.left:null;
            }
        }
        return root;
    }
}
