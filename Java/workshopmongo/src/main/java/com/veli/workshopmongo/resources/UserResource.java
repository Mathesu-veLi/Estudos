package com.veli.workshopmongo.resources;

import com.veli.workshopmongo.domain.User;
import com.veli.workshopmongo.dto.UserDTO;
import com.veli.workshopmongo.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.net.URI;
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

  @RequestMapping(method = RequestMethod.POST)
  public ResponseEntity<Void> insert (@RequestBody UserDTO objDTO) {
    User obj = service.fromDTO(objDTO);
    obj = service.insert(obj);
    URI uri = ServletUriComponentsBuilder.fromCurrentRequest()
                                         .path("/{id}")
                                         .buildAndExpand(obj.getId())
                                         .toUri();
    return ResponseEntity.created(uri).build();
  }
}
