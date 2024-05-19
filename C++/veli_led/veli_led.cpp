#include <Arduino.h>
#include <veli_led.h>

veli_led::veli_led(int pin) {
  this->pin = pin;

  pinMode(this->pin, OUTPUT);
}

void veli_led::on() {
  digitalWrite(this->pin, HIGH);
}

void veli_led::off() {
  digitalWrite(this->pin, LOW);
}

