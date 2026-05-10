-- Table unique_id: id INT default 1, unique; name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
