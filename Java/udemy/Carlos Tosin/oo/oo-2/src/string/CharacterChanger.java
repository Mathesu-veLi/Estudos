package string;

public interface CharacterChanger {
  default String upper(String s) {
    return "*" + s.substring(1);
  }
}
