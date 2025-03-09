package login;

public class ExLogin {
  public static void main(String[] args) {
    StaticLoginMethod l1 = new StaticLoginMethod();
    System.out.println(l1.login("admin", "123"));
    System.out.println(l1.login("admin", "122"));

    SameCredentialsLoginMethod l2 = new SameCredentialsLoginMethod();
    System.out.println(l2.login("user1", "user1"));
    System.out.println(l2.login("user1", "user2"));
  }
}
