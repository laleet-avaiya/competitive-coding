// Check if subtree
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/check-if-subtree/1/?ref=self

class Tree {
    static boolean ans;
    
    public static void inorder(Node a,Node b){
        if(a==null && b==null )
            return;
        if(a==null || b==null)
        {    ans=false;
            return;
            
        }
        inorder(a.left,b.left);
        if(a.data != b.data)
            ans=false;
        inorder(a.right,b.right);
    }
    
    public static void temp(Node node,Node p){
        if(node==null)
            return;
        if(node.data == p.data)
            {ans = true;inorder(node,p);}
        temp(node.left,p);
        temp(node.right,p);
    }
    public static boolean isSubtree(Node T, Node S) {
        // add code here.
        ans = false;
        temp(T,S);
        return ans;
    }
}
