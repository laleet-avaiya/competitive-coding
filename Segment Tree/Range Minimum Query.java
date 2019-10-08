// Range Minimum Query
// 16 June 2019
// https://practice.geeksforgeeks.org/problems/range-minimum-query/1

class GfG {
    static int tree[];

    public static void build(int[] arr, int[] tree, int start, int end, int tree_node) {
        if (start == end) {
            tree[tree_node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        build(arr, tree, start, mid, 2 * tree_node);
        build(arr, tree, mid + 1, end, 2 * tree_node + 1);

        tree[tree_node] = Math.min(tree[2 * tree_node], tree[2 * tree_node + 1]);
    }

    public static int find(int[] tree, int l, int r, int start, int end, int tree_node) {
        if (l > end || r < start)
            return 500000;
        if (l <= start && end <= r)
            return tree[tree_node];
        int mid = (start + end) / 2;
        return (Math.min(find(tree, l, r, start, mid, 2 * tree_node),
                find(tree, l, r, mid + 1, end, 2 * tree_node + 1)));
    }

    public static int[] constructST(int arr[], int n) {
        // Add your code here
        tree = new int[10 * n];
        build(arr, tree, 0, n - 1, 1);
        return tree;
    }

    /*
     * The functions returns the min element in the range from l and r
     */
    public static int RMQ(int st[], int n, int l, int r) {
        return find(st, l, r, 0, n - 1, 1);
    }

}