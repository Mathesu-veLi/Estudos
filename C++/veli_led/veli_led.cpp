#include <Arduino.h>
#include <veli_led.h>

veli_led::veli_led(int pin) {
  this->pin = pin

  pinMode(this->pin, OUTPUT)
}