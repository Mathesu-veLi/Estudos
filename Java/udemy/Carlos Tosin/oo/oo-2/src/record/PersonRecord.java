package record;

import java.util.Objects;

public record PersonRecord(String firstName, String lastName, int age) {
  public PersonRecord {
    Objects.requireNonNull(firstName);
    Objects.requireNonNull(lastName);
  }

  public PersonRecord(String firstName, String lastName) {
    this(firstName, lastName, 0);
  }
}
