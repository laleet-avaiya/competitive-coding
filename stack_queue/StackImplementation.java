// Stack
// Main
import java.util.*;


// class Stack{

//     int[] arr;
//     int top;
//     int numberofelements;

//     Stack(int size){
//         this.arr = new int[size];
//         this.top =0;
//     }

//     public void push(int data){
//         arr[top++] = data;
//         numberofelements++;
//     }

//     public int pop(){
//         numberofelements--;
//         return arr[--top];
//     }
//     public int peek(){
//         return arr[top-1];
//     }

//     public int size(){
//         return this.numberofelements;
//     }
// }

class StackImplementation{

    public static void main(String[] args){
        Stack s = new Stack();

        s.push(5);
        s.push(1);
        s.push(10);
        s.push(55);

        System.out.println(s.pop());
        System.out.println(s.peek());
        s.peek();
        System.out.println(s.empty() + "" + s.peek());
        s.size();
    }
}