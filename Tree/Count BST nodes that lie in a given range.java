// Count BST nodes that lie in a given range 
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1/?ref=self

public static int ans;

public static void inorder(Node node,int left,int right){
    if(node==null)
        return;
    inorder(node.left,left,right);
    if(node.data>=left &&node.data<=right)
        ans+=1;
    inorder(node.right,left,right);
}

public static int getCountOfNode(Node root,int l, int h)
{
    //Your code here
    ans=0;
    inorder(root,l,h);
    return ans;
}
