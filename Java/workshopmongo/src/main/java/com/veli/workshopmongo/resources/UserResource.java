package com.veli.workshopmongo.resources;

import com.veli.workshopmongo.domain.User;
import com.veli.workshopmongo.dto.UserDTO;
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
  public ResponseEntity<List<UserDTO>> findAll () {

    List<User> list = service.findAll();
    List<UserDTO> listDto = list.stream().map(UserDTO::new).toList();
    return ResponseEntity.ok().body(listDto);
  }
}
