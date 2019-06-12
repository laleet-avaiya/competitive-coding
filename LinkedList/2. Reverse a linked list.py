# 2. Reverse a linked list 
# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

def reverseList(self):
    # Code here
    if self.head is None:
        return None
    
    stack=[]
    
    temp=self.head
    
    while temp != None:
        stack.append(temp.data)
        temp=temp.next
        
    temp=self.head
    while temp != None:
        temp.data = stack.pop()
        temp=temp.next
    return self.head




/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

//function Template for Java
/* Return reference of new head of the reverse linked list 
 class Node {
     int value;
    Node next;
    Node(int value) {
        this.value = value;
    }
} */
class gfg
{
    // This function should reverse linked list and return
   // head of the modified linked list.
   Node reverse(Node head)
   {
         if (head == null) {
        return null;
    }
    
    if (head.next == null) {
        return head;
    }
            
    Node preNode = null;
    Node currNode = head;
    Node nextNode = null;
     
    while (currNode != null) {
        nextNode = currNode.next;
        currNode.next = preNode;
        preNode = currNode;
        currNode = nextNode;
    }
    
    head = preNode;
    
    return head;

   }
}
