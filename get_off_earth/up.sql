CREATE TABLE IF NOT EXISTS planets
(
    id                      INT PRIMARY KEY         NOT NULL AUTO_INCREMENT,
    name                    TEXT                    NOT NULL,
    distance                INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ship_types
(
    id                      INT PRIMARY KEY         NOT NULL AUTO_INCREMENT,
    model_name              TEXT                    NOT NULL,
    hypserspeed_rating      INT                     NOT NULL,
    max_capacity            INT                     NOT NULL
);

CREATE TABLE IF NOT EXISTS ships
(
    id                      INT PRIMARY KEY         NOT NULL AUTO_INCREMENT,
    planet_id               INT                     NOT NULL REFERENCES planets(id),
    ship_type_id            INT                     NOT NULL REFERENCES ship_types(id),
    name                    TEXT                    NOT NULL,
    trip_time               INT                     NOT NULL,
    trip_danger             TEXT                    NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets
(
    id                      INT PRIMARY KEY         NOT NULL AUTO_INCREMENT,
    ship_id                 INT                     NOT NULL REFERENCES ships(id),
    name                    TEXT                    NOT NULL,
    pod_quantity            INT                     NOT NULL
);

INSERT INTO planets
(
    id, name, distance
) 
VALUES
(
    (1, "Nibiru", 20),
    (2, "Kepler-22b", 500),
    (3, "Tatooine", 600),
    (4, "Nabu", 1200),
    (5, "Titan III", 2700)
);

INSERT INTO ship_types
(
    id, model_name, hypserspeed_rating, max_capacity
) 
VALUES
(
    (1, "Galactibus", 20, 500),
    (2, "Star-Glider", 50, 90),
    (3, "Pulson", 75, 25),
    (4, "Empirion", 100, 5)
);

INSERT INTO ships
(
    id, planet_id, ship_type_id, name, trip_time, trip_danger
) 
VALUES
(
    (1, 1, 1, "USS Exodus", 1, "Low"),
    (2, 1, 1, "HMS Royal Beacon", 1, "Low"),
    (3, 1, 1, "Great Chinese Voyage", 1, "Low"),
    (4, 2, 2, "USS Empire", 10, "Medium"),
    (5, 2, 2, "SpaceX SuperFalcon 9", 10, "Medium"),
    (6, 3, 2, "Great Chinese Intrepid", 12, "High"),
    (7, 3, 3, "SpaceX MachE II", 8, "High"),
    (8, 4, 3, "Stratocaster", 12, "High"),
    (9, 5, 3, "Benatar", 27, "Medium")
);

INSERT INTO tickets
(
    id, ship_id, name, pod_quantity
) 
VALUES
(
    (NULL, 1, "Lebron James", 2),
    (NULL, 1, "Michael Phelps", 2),
    (NULL, 1, "Dwayne Johnson", 2),
    (NULL, 1, "Jennifer Lawrence", 1),
    (NULL, 2, "Paul McCartney", 1),
    (NULL, 2, "John Lennon", 1),
    (NULL, 2, "Ringo Starr", 1),
    (NULL, 2, "George Harrison", 1),
    (NULL, 3, "Yao Ming", 3),
    (NULL, 3, "Xi Jinping", 5),
    (NULL, 3, "Bruce Lee", 1),
    (NULL, 4, "Cate Blanchet", 1),
    (NULL, 4, "Bradley Cooper", 1),
    (NULL, 4, "Dave Bautista", 2),
    (NULL, 4, "Rob Lowe", 2),
    (NULL, 5, "Jeniffer Lopez", 2),
    (NULL, 5, "George Clooney", 2),
    (NULL, 5, "Kate Hudson", 2),
    (NULL, 6, "Neil DeGrasse Tyson", 1),
    (NULL, 6, "Carl Sagan", 1),
    (NULL, 6, "Jack Ma", 1),
    (NULL, 7, "Elon Musk", 1),
    (NULL, 7, "Jeff Bezos", 1),
    (NULL, 7, "Richard Branson", 1),
    (NULL, 8, "Joe Rogan", 1),
    (NULL, 8, "Sebastian Maniscalco", 1),
    (NULL, 8, "Tom Segura", 1),
    (NULL, 9, "Peter Quill", 1),
    (NULL, 9, "Drax", 1),
    (NULL, 9, "Mantis", 1),
    (NULL, 9, "Nebula", 1),
);