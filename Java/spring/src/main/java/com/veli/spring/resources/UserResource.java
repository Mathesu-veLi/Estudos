package com.veli.spring.resources;

import com.veli.spring.entities.User;
import com.veli.spring.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/users")
public class UserResource {
  @Autowired
  private UserService service;

  @GetMapping
  public ResponseEntity<List<User>> findAll () {
    List<User> list = service.findAll();
    return ResponseEntity.ok().body(list);
  }
}
