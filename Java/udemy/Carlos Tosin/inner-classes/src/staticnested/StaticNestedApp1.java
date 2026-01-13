package staticnested;

public class StaticNestedApp1 {
    public static void main(String[] args) {
        Operation op = new Operation(5, 7);

        int result = op.sum();
        op.sum();

        System.out.println(result);

        System.out.println(op.getCounter().getValue());
    }
}
