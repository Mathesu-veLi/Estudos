#include <Arduino.h>
#include <veli_ultrasonic.h>

veli_ultrasonic::veli_ultrasonic(int pinTrigger, int pinEcho) {
  this -> pinTrigger = pinTrigger;
  this -> pinEcho = pinEcho;
  pinMode(pinTrigger, OUTPUT);
  pinMode(pinEcho)
}