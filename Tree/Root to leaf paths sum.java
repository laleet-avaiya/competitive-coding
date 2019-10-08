// Root to leaf paths sum
// 18 June 2019
// https://practice.geeksforgeeks.org/problems/root-to-leaf-paths-sum/1/?ref=self

class GfG
{
    int fun(Tree node,int curr){
    if(node == null)
        return curr;
    return fun(node.left,(curr*10)+node.data)+fun(node.right,(curr*10)+node.data);
    }
    
	public int treePathsSum(Tree node)
    {
        return fun(node,0)/2;
	}
}