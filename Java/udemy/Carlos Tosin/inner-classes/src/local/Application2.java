package local;

public class Application2 {
    private final String message = "Hi";

    public void greet(String name) {
        class Greeter {
            public void sayHi() {
                System.out.format("%s, %s", message, name);
            }
        }

        Greeter greeter = new Greeter();
        greeter.sayHi();
    }
}
