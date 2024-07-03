package com.veli.workshopmongo.services;

import com.veli.workshopmongo.domain.Post;
import com.veli.workshopmongo.repository.PostRepository;
import com.veli.workshopmongo.services.exception.ObjectNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class PostService {
  @Autowired
  private PostRepository repo;


  public Post findById (String id) {
    Optional<Post> post = repo.findById(id);
    if (post.isEmpty()) {
      throw new ObjectNotFoundException("Object not found");
    }
    return post.get();
  }
}
