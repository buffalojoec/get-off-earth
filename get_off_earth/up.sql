CREATE TABLE IF NOT EXISTS planets
(
    id                      SERIAL PRIMARY KEY      NOT NULL,
    name                    TEXT                    NOT NULL,
    distance                INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ship_types
(
    id                      SERIAL PRIMARY KEY      NOT NULL,
    model_name              TEXT                    NOT NULL,
    hypserspeed_rating      INT                     NOT NULL,
    max_capacity            INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ships
(
    id                      SERIAL PRIMARY KEY      NOT NULL,
    planet_id               INT                     NOT NULL REFERENCES planets(id),
    ship_type_id            INT                     NOT NULL REFERENCES ship_types(id),
    name                    TEXT                    NOT NULL,
    trip_time               INT                     NOT NULL,
    trip_danger             TEXT                    NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets
(
    id                      SERIAL PRIMARY KEY      NOT NULL,
    ship_id                 INT                     NOT NULL REFERENCES ships(id),
    name                    TEXT                    NOT NULL,
    pod_quantity            INT                     NOT NULL
);

INSERT INTO planets
(
    name, distance
) 
VALUES
    ('Nibiru', 20),
    ('Kepler-22b', 500),
    ('Tatooine', 600),
    ('Nabu', 1200),
    ('Titan III', 2700);

INSERT INTO ship_types
(
    model_name, hypserspeed_rating, max_capacity
) 
VALUES
    ('Galactibus', 20, 500),
    ('Star-Glider', 50, 90),
    ('Pulson', 75, 25),
    ('Empirion', 100, 5);

INSERT INTO ships
(
    planet_id, ship_type_id, name, trip_time, trip_danger
) 
VALUES
    (1, 1, 'USS Exodus', 1, 'Low'),
    (1, 1, 'HMS Royal Beacon', 1, 'Low'),
    (1, 1, 'Great Chinese Voyage', 1, 'Low'),
    (2, 2, 'USS Empire', 10, 'Medium'),
    (2, 2, 'SpaceX SuperFalcon 9', 10, 'Medium'),
    (3, 2, 'Great Chinese Intrepid', 12, 'High'),
    (3, 3, 'SpaceX MachE II', 8, 'High'),
    (4, 3, 'Stratocaster', 12, 'High'),
    (5, 3, 'Benatar', 27, 'Medium');

INSERT INTO tickets
(
    ship_id, name, pod_quantity
) 
VALUES
    (1, 'Lebron James', 2),
    (1, 'Michael Phelps', 2),
    (1, 'Dwayne Johnson', 2),
    (1, 'Jennifer Lawrence', 1),
    (2, 'Paul McCartney', 1),
    (2, 'John Lennon', 1),
    (2, 'Ringo Starr', 1),
    (2, 'George Harrison', 1),
    (3, 'Yao Ming', 3),
    (3, 'Xi Jinping', 5),
    (3, 'Bruce Lee', 1),
    (4, 'Cate Blanchet', 1),
    (4, 'Bradley Cooper', 1),
    (4, 'Dave Bautista', 2),
    (4, 'Rob Lowe', 2),
    (5, 'Jeniffer Lopez', 2),
    (5, 'George Clooney', 2),
    (5, 'Kate Hudson', 2),
    (6, 'Neil DeGrasse Tyson', 1),
    (6, 'Carl Sagan', 1),
    (6, 'Jack Ma', 1),
    (7, 'Elon Musk', 1),
    (7, 'Jeff Bezos', 1),
    (7, 'Richard Branson', 1),
    (8, 'Joe Rogan', 1),
    (8, 'Sebastian Maniscalco', 1),
    (8, 'Tom Segura', 1),
    (9, 'Peter Quill', 1),
    (9, 'Drax', 1),
    (9, 'Mantis', 1),
    (9, 'Nebula', 1);