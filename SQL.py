
CREATE TABLE movies (
  id INT NOT NULL PRIMARY KEY,
  title VARCHAR(200),
  year INT
);

CREATE TABLE actors (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(75)
);

CREATE TABLE appearences (
  id INT NOT NULL PRIMARY KEY,
  actor_id INT NOT NULL,
  movie_id INT NOT NULL
);

CREATE TABLE award (
  id INT NOT NULL PRIMARY KEY,
  appearence_id INT NOT NULL,
  award_name VARCHAR(200) NOT NULL,
  award_body VARCHAR (100) NOT NULL
);

ALTER TABLE appearences
ADD CONSTRAINT fk_appearences_actors
FOREIGN KEY (actor_id)
REFERENCES actors(id);


ALTER TABLE appearences
ADD CONSTRAINT fk_appearences_movies
FOREIGN KEY (movie_id)
REFERENCES movies(id);

ALTER TABLE award
ADD CONSTRAINT fk_award_appearences
FOREIGN KEY (appearence_id)
REFERENCES appearences(id);

INSERT INTO movies(id, title, year)
VALUES 
      (1, 'Titanic', 2007),
      (2, 'Lord of the rings', 2012);

INSERT INTO actors(id, name)
VALUES
      (1, 'Leonardo di caprio'),
      (2, 'Kate Winslet'),
      (3, 'Orlando bloom'),
      (4, 'Ian McKellen');

INSERT INTO appearences(id, movie_id, actor_id)
VALUES 
      (1, 1, 1),
      (2, 1, 2),
      (3, 2, 3),
      (4, 2, 4),
      (5, 1, 4);

INSERT INTO award(id, appearence_id, award_name, award_body)
VALUES
      (1, 1, 'best leading male actor', 'oscar'),
      (3, 3, 'best accompnying actor', 'bafta'), 
      (4, 4, 'best wizard in movie', 'bafta');


SELECT ac.name
FROM actors AS ac inner JOIN appearences AS ap ON ac.id = ap.actor_id
inner JOIN movies  AS m ON m.id = ap.movie_id
WHERE m.title = 'Titanic';

SELECT ac.name actor, COUNT(ap.id) number_movies
FROM actors AS ac inner JOIN appearences AS ap ON ac.id = ap.actor_id
GROUP BY ac.name;

SELECT ac.name, m.title, a.award_body , a.award_name
FROM actors AS ac inner JOIN  appearences AS ap ON ac.id = ap.actor_id inner JOIN movies AS m ON ap.movie_id = m.id inner JOIN award AS a ON ap.id = a.appearence_id;

