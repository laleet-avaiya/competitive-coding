// Full binary tree 
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/full-binary-tree/1


class GfG
{   
    static boolean ans;
    void inorder(Node node){
        if(node==null)
            return;
        if(node.left!=null && node.right==null)ans=false;
        if(node.right!=null && node.left==null)ans=false;
        inorder(node.left);
        inorder(node.right);
    }
	boolean isFullTree(Node node)
    {
        //add code here
        ans = true;
        inorder(node);
        return ans;
        
    }
}