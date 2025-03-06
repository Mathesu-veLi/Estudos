package br.com.javainsider.other;

public class Lamp {
  private boolean on;

  public Lamp (boolean on) {
    this.on = on;
  }

  public void showState () {
    System.out.println("Lâmpada " + (on ? "ligada" : "desligada"));
  }

  public void turnOn () {
    this.on = true;
  }

  public void turnOff() {
    this.on = false;
  }
}
