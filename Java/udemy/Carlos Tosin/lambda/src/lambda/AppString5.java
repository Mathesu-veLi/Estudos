package lambda;

public class AppString5 {
    public static void main(String[] args) {
        createAndPrint(Person::new, "Levi");
    }

    private static void createAndPrint(PersonCreator creator, String name) {
        System.out.println(creator.create(name));
    }
}
