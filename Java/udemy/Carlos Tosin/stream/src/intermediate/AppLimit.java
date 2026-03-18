package intermediate;

public class AppLimit {
    public static void main(String[] args) {
        var names = Student.list()
            .stream()
            .map(Student::name)
            .sorted()
            .limit(20)
            .toList();

        System.out.println(names);
    }
}
