package com.veli.workshopmongo.resources;

import com.veli.workshopmongo.domain.Post;
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

  @RequestMapping(value = "/{id}", method = RequestMethod.GET)
  public ResponseEntity<UserDTO> findById (@PathVariable String id) {
    User obj = service.findById(id);
    return ResponseEntity.ok().body(new UserDTO(obj));
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

  @RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
  public ResponseEntity<Void> delete (@PathVariable String id) {
    service.delete(id);
    return ResponseEntity.noContent().build();
  }

  @RequestMapping(value = "/{id}", method = RequestMethod.PUT)
  public ResponseEntity<Void> update (@RequestBody UserDTO objDTO, @PathVariable String id) {
    User obj = service.fromDTO(objDTO);
    obj.setId(id);
    obj = service.update(obj);
    return ResponseEntity.noContent().build();
  }


  @RequestMapping(value = "/{id}/posts", method = RequestMethod.GET)
  public ResponseEntity<List<Post>> findPosts (@PathVariable String id) {
    User obj = service.findById(id);
    return ResponseEntity.ok().body(obj.getPosts());
  }
}