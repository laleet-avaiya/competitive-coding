//  Find Median from Data Stream
//  https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder {
    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;

    /** initialize your data structure here. */
    public MedianFinder() {
        this.lo = new PriorityQueue<Integer>(); // max
        this.hi = new PriorityQueue<Integer>(); // min
    }

    public void addNum(int num) {
        lo.add(-num);
        hi.add(-lo.poll());

        if (lo.size() < hi.size()) {
            lo.add(-hi.poll());
        }
    }

    public double findMedian() {
        return lo.size() > hi.size() ? (double) -lo.peek() : (-lo.peek() + hi.peek()) * 0.5;
    }
}