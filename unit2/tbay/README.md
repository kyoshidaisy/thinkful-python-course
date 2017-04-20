Model an Auction Site Using SQLAlchemy
https://courses.thinkful.com/pip-001v3/assignment/2.2

**-- tbay SQLAlchemy project --**


_In the previous lesson you learned how to communicate with a PostgreSQL database by writing SQL statements, at first using the command line, and later on from inside Python itself. As you were working on the snippets app you probably noticed that it felt like you were writing in two different languages, switching between Python syntax and SQL syntax.

In this lesson you will learn SQLAlchemy, a module which is designed to bridge the gap between Python and SQL. You'll write Python classes and create instances of those classes. In the background SQLAlchemy will be transforming these actions into the SQL statements which you learned in the previous lesson, and using them to build a database.

Along the way you will be building the database layer for the world's second most popular auction site, TBay. You will create users, have them put items up for auction, and place bids to try to win the items which are up for sale.

Goals

Use SQLAlchemy to create tables and rows
Query a database using SQLALchemy
Create relationships between models_