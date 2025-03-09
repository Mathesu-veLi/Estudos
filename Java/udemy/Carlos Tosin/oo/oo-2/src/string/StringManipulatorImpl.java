package string;

public class StringManipulatorImpl implements StringManipulator {
  @Override
  public String join(String s1, String s2) {
    return s1 + s2;
  }

  @Override
  public String takeFirst(String s, int length) {
    return s.substring(0, length);
  }
}
