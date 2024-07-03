package com.veli.workshopmongo.services;

import com.veli.workshopmongo.domain.User;
import com.veli.workshopmongo.dto.UserDTO;
import com.veli.workshopmongo.repository.UserRepository;
import com.veli.workshopmongo.services.exception.ObjectNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {
  @Autowired
  private UserRepository repo;

  public List<User> findAll () {
    return repo.findAll();
  }

  public User findById (String id) {
    Optional<User> user = repo.findById(id);
    if (user == null) {
      throw new ObjectNotFoundException("Object not found");
    }
    return user.get();
  }

  public User insert (User obj) {
    return repo.insert(obj);
  }

  public User fromDTO (UserDTO objDTO) {
    return new User(objDTO.getId(), objDTO.getName(), objDTO.getEmail());
  }
}
