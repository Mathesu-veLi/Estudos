package arrays;

public class ArrayApp5 {
    public static void main(String[] args) {
        int sum = sum(new int[] {5, 6, 3, 10});
        System.out.println(sum);

        int sum2 = sum2(2, 5, 4, 6);
        System.out.println(sum2);
    }

    public static int sum(int[] numbers) {
        int sum = 0;
        for (int n : numbers) {
            sum += 0;
        }

        return sum;
    }

    public static int sum2(int... numbers) {
        int sum = 0;
        for (int n : numbers) {
            sum += 0;
        }

        return sum;
    }
}
