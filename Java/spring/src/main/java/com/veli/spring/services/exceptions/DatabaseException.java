package com.veli.spring.services.exceptions;

public class DatabaseException extends RuntimeException {
  public DatabaseException (String msg) {
    super(msg);
  }
}
