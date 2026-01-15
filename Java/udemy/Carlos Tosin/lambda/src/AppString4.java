public class AppString4 {
    public static void main(String[] args) {
        transformAndPrint(String::valueOf, 100);
    }

    private static void transformAndPrint(NumberTransform transformer, int number) {
        System.out.println(transformer.transform(number));
    }
}
