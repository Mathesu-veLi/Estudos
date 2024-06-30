package com.veli.spring.resources;

import com.veli.spring.entities.User;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "/users")
public class UserResource {
  @GetMapping
  public ResponseEntity<User> findAll () {
    User u = new User(1L, "Maria", "maria@gmail.com", "9999999", "12345");
    return ResponseEntity.ok().body(u);
  }
}
