
/*package whatever //do not write package name here */
import java.util.*;
import java.io.*;

class Example {

    public static int Root(int[] Arr, int i) {
        while (Arr[i] != i) {
            i = Arr[i];
        }
        return i;
    }

    public static void Union(int[] Arr, int A, int B) {
        int RootA = Root(Arr, A);
        int RootB = Root(Arr, B);

        Arr[RootB] = RootA;
    }

    public static boolean Find(int[] Arr, int A, int B) {
        if (Root(Arr, A) == Root(Arr, B))
            return true;
        return false;
    }

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int M = s.nextInt();
        int[] Arr = new int[N];
        for (int i = 0; i < N; i++)
            Arr[i] = i;

        while (M-- > 0) {
            int x = s.nextInt();
            int y = s.nextInt();

            Union(Arr, x, y);
        }

        for (int a : Arr)
            System.out.print(a + " ");

    }
}