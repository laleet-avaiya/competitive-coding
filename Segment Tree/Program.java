import java.util.*;

import javax.management.Query;

/**
 * SegmentTree
 */
class SegmentTree {
    public int[] tree;
    public int size;

    public SegmentTree(int[] arr, int size) {
        this.tree = new int[2 * size];
        this.size = 2 * size;
        BuildTree(arr, 0, size - 1, 1);
    }

    public void BuildTree(int[] arr, int start, int end, int tree_node) {
        if (start == end) {
            this.tree[tree_node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        BuildTree(arr, start, mid, 2 * tree_node);
        BuildTree(arr, mid + 1, end, 2 * tree_node + 1);
        this.tree[tree_node] = tree[2 * tree_node] + tree[2 * tree_node + 1];
    }

    public void printTree() {
        for (int i = 1; i < tree.length; i++)
            System.out.println(tree[i] + " ");
    }

    public void update(int index, int value) {
        UpdateTree(0, size / 2, 1, index, value);
    }

    public void UpdateTree(int start, int end, int tree_node, int index, int value) {
        if (start == end) {
            this.tree[tree_node] += value;
            return;
        }
        int mid = (start + end) / 2;
        if (index <= mid)
            UpdateTree(start, mid, 2 * tree_node, index, value);
        else
            UpdateTree(mid + 1, end, 2 * tree_node + 1, index, value);

        this.tree[tree_node] = tree[2 * tree_node] + tree[2 * tree_node + 1];
    }

    public int query(int left, int right) {
        return Query(0, size / 2, left, right, 1);
        // 1. Range represented by a node is completely outside the given range
        // 2. Range represented by a node is completely inside the given range
        // 3. Range represented by a node is partially inside and partially outside the given range
    }

    public int Query(int start, int end, int left, int right, int tree_node) {

        // 1. Range represented by a node is completely outside the given range
        if (right < start || left > end)
            return 0;

        // 2. Range represented by a node is completely inside the given range
        if (left <= start && end <= right)
            return tree[tree_node];

        // 3. Range represented by a node is partially inside and partially outside the given range
        int mid = (start + end) / 2;
        int a = Query(start, mid, left, right, 2 * tree_node);
        int b = Query(mid + 1, end, left, right, 2 * tree_node + 1);
        return (a + b);
    }

}

class Program {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = s.nextInt();

        // Build
        SegmentTree t = new SegmentTree(a, n);
        t.printTree();

        // Update
        int index = 9;
        int value = -9;
        a[index - 1] += value;
        t.update(index, value);
        t.printTree();

        // Query
        int l = 0;
        int r = n - 1;
        System.out.println(t.query(l, r));
        

    }
}