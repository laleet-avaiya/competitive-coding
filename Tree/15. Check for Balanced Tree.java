// Check for Balanced Tree 
// https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1

class GfG
{
    
     /* This function should return tree if passed  tree 
     is balanced, else false. */
    int height(Node root){
    if(root==null)
        return 0;
    return Math.max(height(root.left),height(root.right))+1;
    }


    boolean isBalanced(Node root)
    {
	// Your code here
	if(root==null)
        return true;
    return isBalanced(root.left) && isBalanced(root.right) && Math.abs(height(root.left)-height(root.right))<2;

    }
}
