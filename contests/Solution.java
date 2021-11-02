package contests;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Solution {
    static class State implements Comparable<State> {
        public int distance;
        public int city;
    
        public State(int distance, int city){
            this.distance = distance;
            this.city = city;
        }
        @Override
        public int compareTo(State o) {
            if (this.distance > o.distance) return 1;
            else if (o.distance > this.distance) return -1;
            return 0;
        }
    }
    static void policeStations(int d, HashSet<Integer> stations, HashMap<Integer, ArrayList<State>> adj_list) {
        PriorityQueue<State> queue = new PriorityQueue<>();
        HashSet<Integer> visited = new HashSet<>();

        for (int s : stations) {
            visited.add(s);
            queue.add(new State(0, s));
        }
        HashSet<Integer> removed = new HashSet<>();
        HashSet<Integer> finalVisited = new HashSet<>();
        while (queue.size() != 0) {
            State pair = queue.poll();
            finalVisited.add(pair.city);
            if (pair.distance == d) continue;
            for (State newPair : adj_list.get(pair.city)){
                int road = newPair.distance;
                int nbr = newPair.city;
                if (!finalVisited.contains(nbr) && ((visited.contains(nbr) || stations.contains(nbr))))removed.add(road);
                else if (!visited.contains(nbr)){
                    visited.add(nbr);
                    queue.add(new State(pair.distance+1, nbr));
                }
            }
        }
        System.out.println(removed.size());
        for (int road: removed) System.out.print(road+" ");
        

    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int d = Integer.parseInt(input[2]);
        
        HashSet<Integer> stations = new HashSet<>();
        String[] line = scanner.nextLine().split(" ");
        for (String l : line) stations.add(Integer.parseInt(l));
        HashMap<Integer, ArrayList<State>> adj_list = new HashMap<>();
        for (int i = 0; i < n; ++i) adj_list.put(i+1, new ArrayList<State>());
        for (int i = 0; i < n-1; ++i){
            String[] edge = scanner.nextLine().split(" ");
            int start = Integer.parseInt(edge[0]);
            int dest = Integer.parseInt(edge[1]);
            adj_list.get(start).add(new State(i+1, dest));
            adj_list.get(dest).add(new State(i+1, start));
        }
        policeStations(d, stations, adj_list);
        scanner.close();
    }
}
