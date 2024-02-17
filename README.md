# Register and LogIn System (In development)

## What is the project?

Register and login system project using python as programming language and PostgreSQL as RDBMS.
Using the MVC pattern, the system was developed to avoid dupliucated email accounts insertions and uses a hash + salting algorithm to encypt the password users.
 
## Softwares and packages used

**Python** is the programming language uused to devolop the project.  
**SQLAlchemy** it's a ORM library for python, allowing easy connection between RDBMS and a Python class representing a table in the database.  
**Psycopg2** is a Python library that provide connection with PostgreSQL, in the project, is used for **SQLAlchemy** to identify what RDBMS we're using.  
**Argon2** is a password hashing algorithm available for Python and others languages. By the fact that store the "real" user's password in the database is such a bad idea, Argon2 it's an awesome option to avoid this mistake, by default, this algorithm uses hashing + salting, this means that the database will store different hashes for any users even if this users create the same password in the register step, wich difficult more on a possible invasion of the database.  
**PostgreSQL** it's a open-source RDBMS for SQL databases, reliable, robust, performatic
**pgAdmin 4** allow us to administrate and develop PostgreSQL databases.

## How to try (In development)



## Examples (In development)