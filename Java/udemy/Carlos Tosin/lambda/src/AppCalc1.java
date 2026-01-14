public class AppCalc1 {
    public static void main(String[] args) {
        Operation sum = new Operation() {
            @Override
            public int calculate(int n1, int n2) {
                return n1 + n2;
            }
        };

        Operation mult = (n1, n2) -> n1 * n2;

        run(sum);
        run(mult);
    }

    private static void run(Operation operation) {
        int r = operation.calculate(5, 4);
        System.out.println(r);
    }
}
