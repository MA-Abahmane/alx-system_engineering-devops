-- An sql script to Create a MySQL user named holberton_user on a server and sets the host name set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.

CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
