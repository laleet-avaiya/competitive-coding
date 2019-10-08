// Clone a linked list with next and random pointer
// 18 July 2019
// https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1


class Clone {
    Node copyList(Node head1) {
        // your code here
        

        // 1) Create the copy of node 1 and insert it between node 1 & node 2 
        // in original Linked List, create the copy of 2 and insert it between 2 & 3..
        // Continue in this fashion, add the copy of N afte the Nth node
        
        Node a = head1;
        
        while(a!=null)
        {
            Node copy = new Node(a.data);
            
            copy.next = a.next;
            a.next = copy;
            
            a = copy.next;
        }
        
        
        // set arbitary pointer / Now copy the arbitrary link 
        
        Node q = head1;
        
        while(q!=null)
        {
            if(q.arb!=null)
            {
                q.next.arb = q.arb.next;
                q = q.next.next;
            }else{
                q.next.arb = null;
                q = q.next.next;
            }
        }
        
        // seprate them /  Now restore the original and copy linked lists in a single loop
        
        Node copyHead = head1.next;
        q = head1;
        
        while(q!=null)
        {
            Node temp = q.next;
            q.next = temp.next;
            
            if(temp.next!=null)
                    temp.next = temp.next.next;
                    
            q = q.next;
            
        }
      
        
      
        return copyHead;


    }
}
