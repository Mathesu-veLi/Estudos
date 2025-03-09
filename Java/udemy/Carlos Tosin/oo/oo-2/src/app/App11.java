package app;

import record.Person;
import record.PersonRecord;

public class App11 {
  public static void main(String[] args) {
    Person person = new Person("José", "Silva", 32);
    System.out.println(person);

    PersonRecord personRecord = new PersonRecord("José", "Silva", 32);
    System.out.println(personRecord);

    PersonRecord personRecord2 = new PersonRecord("José", "Silva", 33);
    System.out.println(personRecord2.equals(personRecord));
  }
}
