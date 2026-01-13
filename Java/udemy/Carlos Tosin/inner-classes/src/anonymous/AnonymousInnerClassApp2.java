package anonymous;

public class AnonymousInnerClassApp2 {
    public static void main(String[] args) {
        Food f1 = new Food();
        f1.eat();

        Food f2 = new Food() {
            @Override
            public void eat() {
                System.out.println("Eating fish!");
            }
        };
        f2.eat();
    }
}
