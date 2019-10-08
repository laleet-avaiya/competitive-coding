// Construct Tree from Preorder Traversal 
// 16 June 2019
// https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1


class GFG
{
    Node constructTree(int n, int pre[], char preLN[])
    {
	    //Add your code here.
	    
	    // 1st element is a root
	    java.util.Stack<Node> s = new java.util.Stack<>();
	    Node root = new Node(pre[0]);
	    s.push(root);
	    
	    int i=1;
	    while(i<n && !s.isEmpty()){
	        Node newnode = new Node(pre[i]);
	        Node p = s.peek();
	        if(p.left!=null){
	            p.right = newnode;
	            s.pop();
	        }else{
	            p.left = newnode;
	        }
	        
	        if(preLN[i]=='N')
	            s.push(newnode);
	        i++;   
	    }
	    
	    return root;
	    
    }
}