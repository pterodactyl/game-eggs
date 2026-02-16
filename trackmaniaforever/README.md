# Trackmania Nations/United Forever server with XASECO

This egg requires a running MySQL/MariaDB instance for XASECO, you can easily install one using the MariaDB egg from Pterodactyl (tested on 10.6).

You will need to run commands inside the SQL server to create a user and a database for XASECO. If the server is in pterodactyl, you can do that using the server management console.

```
CREATE DATABASE aseco;
CREATE USER 'tmf';
SET PASSWORD FOR 'tmf' = password('password');
GRANT all ON aseco.* TO 'tmf';
```

Username and password are configurable in the egg variables.
