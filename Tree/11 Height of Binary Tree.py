# Height of Binary Tree
# https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

# int height(Node node) 
#     {
#          // Your code here
#          if(node==null)
#             return 0;
#          return 1 + Math.max(height(node.left),height(node.right));
#     }   