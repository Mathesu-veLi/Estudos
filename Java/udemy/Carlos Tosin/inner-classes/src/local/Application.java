package local;

public class Application {
    public void greet() {
        class Greeter {
            public void sayHi() {
                System.out.println("Hi!");
            }
        }

        Greeter greeter = new Greeter();
        greeter.sayHi();
    }
}
