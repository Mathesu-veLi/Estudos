package anonymous;

public class ExRunnable {
    public static void main(String[] args) {
        doIt(new Runnable() {
            @Override
            public void run() {
                System.out.println("Hi!");
            }
        });

        doIt(new Runnable() {
            @Override
            public void run() {
                System.out.println(Math.random());
            }
        });
    }

    private static void doIt(Runnable runnable) {
        System.out.println("Running...");
        runnable.run();
    }
}
