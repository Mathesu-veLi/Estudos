package intermediate;

import java.util.List;

public class ExPassFail {
    public static void main(String[] args) {
        var students = List.of(
            new Student("José", List.of(8.5, 10.0, 9.0)), new Student("Pedro", List.of(7.0, 7.0, 7.0)),
            new Student("Maria", List.of(6.5, 9.0, 4.0)), new Student("Sara", List.of(4.5, 3.0, 6.5))
        );

        students
            .stream()
            .map(s -> {
                double avg = s
                    .grades()
                    .stream()
                    .mapToDouble(g -> g)
                    .average()
                    .orElse(0);
                boolean pass = avg >= 7.0;
                return s.name + " - " + (pass ? "PASS" : "FAIL");
            })
            .forEach(System.out::println);
    }

    private record Student(String name, List<Double> grades) { }
}
