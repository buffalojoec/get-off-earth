CREATE TABLE IF NOT EXISTS planets
(
    id                      SERIAL PRIMARY KEY,
    name                    TEXT                    NOT NULL,
    distance                INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ship_types
(
    id                      SERIAL PRIMARY KEY,
    model_name              TEXT                    NOT NULL,
    hypserspeed_rating      INT                     NOT NULL,
    max_capacity            INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ships
(
    id                      SERIAL PRIMARY KEY,
    planet_id               INT                     NOT NULL REFERENCES planets(id),
    ship_type_id            INT                     NOT NULL REFERENCES ship_types(id),
    name                    TEXT                    NOT NULL,
    trip_time               INT                     NOT NULL,
    trip_danger             TEXT                    NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets
(
    id                      SERIAL PRIMARY KEY,
    ship_id                 INT                     NOT NULL REFERENCES ships(id),
    name                    TEXT                    NOT NULL,
    pod_quantity            INT                     NOT NULL
);

INSERT INTO planets
(
    id, name, distance
) 
VALUES
    (DEFAULT, 'Nibiru', 20),
    (DEFAULT, 'Kepler-22b', 500),
    (DEFAULT, 'Tatooine', 600),
    (DEFAULT, 'Nabu', 1200),
    (DEFAULT, 'Titan III', 2700);

INSERT INTO ship_types
(
    id, model_name, hypserspeed_rating, max_capacity
) 
VALUES
    (DEFAULT, 'Galactibus', 20, 500),
    (DEFAULT, 'Star-Glider', 50, 90),
    (DEFAULT, 'Pulson', 75, 25),
    (DEFAULT, 'Empirion', 100, 5);

INSERT INTO ships
(
    id, planet_id, ship_type_id, name, trip_time, trip_danger
) 
VALUES
    (DEFAULT, 1, 1, 'USS Exodus', 1, 'Low'),
    (DEFAULT, 1, 1, 'HMS Royal Beacon', 1, 'Low'),
    (DEFAULT, 1, 1, 'Great Chinese Voyage', 1, 'Low'),
    (DEFAULT, 2, 2, 'USS Empire', 10, 'Medium'),
    (DEFAULT, 2, 2, 'SpaceX SuperFalcon 9', 10, 'Medium'),
    (DEFAULT, 3, 2, 'Great Chinese Intrepid', 12, 'High'),
    (DEFAULT, 3, 3, 'SpaceX MachE II', 8, 'High'),
    (DEFAULT, 4, 3, 'Stratocaster', 12, 'High'),
    (DEFAULT, 5, 3, 'Benatar', 27, 'Medium');

INSERT INTO tickets
(
    id, ship_id, name, pod_quantity
) 
VALUES
    (DEFAULT, 1, 'Lebron James', 2),
    (DEFAULT, 1, 'Michael Phelps', 2),
    (DEFAULT, 1, 'Dwayne Johnson', 2),
    (DEFAULT, 1, 'Jennifer Lawrence', 1),
    (DEFAULT, 2, 'Paul McCartney', 1),
    (DEFAULT, 2, 'John Lennon', 1),
    (DEFAULT, 2, 'Ringo Starr', 1),
    (DEFAULT, 2, 'George Harrison', 1),
    (DEFAULT, 3, 'Yao Ming', 3),
    (DEFAULT, 3, 'Xi Jinping', 5),
    (DEFAULT, 3, 'Bruce Lee', 1),
    (DEFAULT, 4, 'Cate Blanchet', 1),
    (DEFAULT, 4, 'Bradley Cooper', 1),
    (DEFAULT, 4, 'Dave Bautista', 2),
    (DEFAULT, 4, 'Rob Lowe', 2),
    (DEFAULT, 5, 'Jeniffer Lopez', 2),
    (DEFAULT, 5, 'George Clooney', 2),
    (DEFAULT, 5, 'Kate Hudson', 2),
    (DEFAULT, 6, 'Neil DeGrasse Tyson', 1),
    (DEFAULT, 6, 'Carl Sagan', 1),
    (DEFAULT, 6, 'Jack Ma', 1),
    (DEFAULT, 7, 'Elon Musk', 1),
    (DEFAULT, 7, 'Jeff Bezos', 1),
    (DEFAULT, 7, 'Richard Branson', 1),
    (DEFAULT, 8, 'Joe Rogan', 1),
    (DEFAULT, 8, 'Sebastian Maniscalco', 1),
    (DEFAULT, 8, 'Tom Segura', 1),
    (DEFAULT, 9, 'Peter Quill', 1),
    (DEFAULT, 9, 'Drax', 1),
    (DEFAULT, 9, 'Mantis', 1),
    (DEFAULT, 9, 'Nebula', 1);