package random;

public class RandomApp2 {
    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            int d = random(0,5);
            System.out.println(d);
        }
    }

    private static int random(int from, int to) {
        int range = to - from + 1;
        return (int) (Math.random() * range) + from;
    }
}
