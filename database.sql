DROP TABLE IF EXISTS urls CASCADE;
DROP TABLE IF EXISTS url_checks;

CREATE TABLE urls (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE url_checks (
    id BIGSERIAL PRIMARY KEY,
    url_id BIGINT REFERENCES urls (id),
    status_code SMALLINT,
    h1 VARCHAR(255),
    title VARCHAR(255),
    description VARCHAR(255),
    created_at DATE DEFAULT CURRENT_DATE
);
