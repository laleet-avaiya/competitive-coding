// Find median in a stream
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
    static class MedianFinder {
        PriorityQueue<Integer> lo;
        PriorityQueue<Integer> hi;
    
        /** initialize your data structure here. */
        public MedianFinder() {
            this.lo = new PriorityQueue<Integer>(Collections.reverseOrder()); // max
            this.hi = new PriorityQueue<Integer>(); // min
        }
    
        public void addNum(int num) {
            lo.add(num);
            hi.add(lo.poll());
    
            if (lo.size() < hi.size()) {
                lo.add(hi.poll());
            }
        }

    public double findMedian() {
        return lo.size() > hi.size() ? (double) lo.peek() : (lo.peek() + hi.peek()) * 0.5;
    }
}


	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int n = s.nextInt();
		MedianFinder a = new MedianFinder();
		
		while(n-->0)
		{
		    a.addNum(s.nextInt());
		    int ans = (int)a.findMedian();
		    System.out.println(ans);
		}
	}
}