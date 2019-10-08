import java.util.*;
import java.lang.*;
import java.io.*;


class Temp implements Comparator<Temp> {
    public int key;
    public int ver;

    public Temp(int key, int ver) {
        this.key = key;
        this.ver = ver;
    }


    @Override
    public int compare(Temp a, Temp b) {
        return a.key - b.key;
    }
}



class MinHeap {

    public static void main(String[] args) {
        PriorityQueue<Temp> a = new PriorityQueue<>();

        int[][] v = {{6,0,7,0,0},
                    {0,5,8,-4,0},
                    {-2,0,0,0,0},
                    {0,-3,0,0,0},
                    {0,7,0,0,0}};

        boolean[] vis = new boolean[5];
        int[] dist = new int[5];
        dist[0]=0;

        a.add(new Temp(0,0));

        while(!a.isEmpty()){

            Temp p = a.poll();

            int ver = p.ver;
            int wei = p.key;

            if( vis[ver] ) continue;                  // check if the popped vertex is visited before
            vis[ver] = true;


            for(int i = 0; i < v[ver].length; i++){
                if(dist[ver] + v[ver][i] < dist[i]){            // check if the next vertex distance could be minimized
                    dist[i] = dist[ver] + v[ver][i];
                    a.add(new Temp(dist[i],  i));           // insert the next vertex with the updated distance
                }
            }
        }



        for(int i=0;i<dist.length;i++)
            System.out.print(dist[i] + " ");

    }
}