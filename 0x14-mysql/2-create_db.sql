-- Create a database named tyrell_corp, 
-- Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
-- Make sure that holberton_user has SELECT permissions.

CREATE DATABASE tyrell_corp;

CREATE TABLE tyrell_corp.nexus6(
        id INT NOT NULL AUTO_INCREMENT,
        name varchar(20) NOT NULL,
        PRIMARY KEY (id)
);

INSERT INTO tyrell_corp.nexus6(name) VALUES ('Ramadan');


GRANT SELECT ON tyrell_corp.nexus6  TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
