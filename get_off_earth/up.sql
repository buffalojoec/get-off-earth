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