package com.veli.workshopmongo.resources;

import com.veli.workshopmongo.domain.User;
import com.veli.workshopmongo.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/users")
public class UserResource {
  @Autowired
  private UserService service;

  @RequestMapping(method = RequestMethod.GET)
  public ResponseEntity<List<User>> findAll () {

    List<User> list = service.findAll();
    return ResponseEntity.ok().body(list);
  }
}
