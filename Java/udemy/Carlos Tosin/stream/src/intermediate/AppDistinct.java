package intermediate;

public class AppDistinct {
    public static void main(String[] args) {
        var grades = Student.list()
            .stream()
            .flatMap(s -> s.grades()
                .stream())
            .distinct()
            .toList();

        System.out.println(grades);
    }
}
