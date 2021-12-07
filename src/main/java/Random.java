import java.util.HashSet;

public class Random {
    public static void main(String[] args) {
        HashSet<Integer> set1 = new HashSet<Integer>();
        for (int i = 0; i< 5; i++){
            set1.add(i);
        }
        System.out.println(set1);
    }
}
