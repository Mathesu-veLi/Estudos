package com.veli.workshopmongo.resources;

import com.veli.workshopmongo.domain.User;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping(value = "/users")
public class UserResource {
  @RequestMapping(method = RequestMethod.GET)
  public ResponseEntity<List<User>> findAll () {
    User maria = new User("1", "Maria", "maria@gmail.com");
    User alex = new User("2", "Alex", "alex@gmail.com");

    List<User> list = new ArrayList<>(Arrays.asList(maria, alex));
    return ResponseEntity.ok().body(list);
  }
}
