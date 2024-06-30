package app;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import dominio.Pessoa;

public class Main {
	public static void main(String[] args) {
		Pessoa p1 = new Pessoa(null, "Carlos", "carlos@gmail.com");

		EntityManagerFactory emf = Persistence.createEntityManagerFactory("exemplo-jpa");
		EntityManager em = emf.createEntityManager();

		em.getTransaction().begin();
		em.persist(p1);
		em.getTransaction().commit();

		System.out.println("Pronto!");
	}
}
