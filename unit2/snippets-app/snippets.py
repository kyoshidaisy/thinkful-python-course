import psycopg2
import argparse
import logging

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

# connection to database from Python
logging.debug("Conneting to PostgreSQL")
connection = psycopg2.connect(database='snippets')
logging.debug("Database connection established.")


def put(name, snippet, hide=False):
    """
    Store a snippet with an associated name.
        Returns the name and the snippet
    """
    logging.info("Storing snippet {!r}: {!r} - option :{!r}".format(name, snippet, hide))
    with connection, connection.cursor() as cursor:
        try:
            cursor.execute("insert into snippets values (%s, %s, %s)", (name, snippet, hide))
        except psycopg2.IntegrityError as e:
            logging.debug("updating existent entry {!r} -- {!r}".format(name, e))
            connection.rollback()
            cursor.execute("update snippets set message=%s, hidden=%s where keyword=%s", (snippet, hide, name))
            print("Existent snippet {!r} is updated.".format(name))

    logging.debug("Snippet saved successfully")
    return name, snippet


def get(name):
    """Retrieve the snippet with a given name.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet.
    """
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
    logging.debug("Snippet retrieved successfully.")
    if not row:
        # No snippet was found with that name.
        return "404: Snippet Not Found"
    return row[0]


def delete(name):
    """Delete the snippet with a given name with confirmation.
    If there is no such snippet, return '404: Snippet Not Found'.
    Returns the snippet.
    """
    logging.info("Deleting snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("delete from snippets where keyword=%s", (name,))
        connection.commit()
    logging.debug("Snippet deleted successfully.")
    return name


def catalog():
    """
    look up the keywords
    query keywords from snippet table
    """
    logging.info("Retrieving list of names")
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword from snippets where not hidden")
        row = cursor.fetchall()
    logging.debug("Snippet names retrieved successfully.")
    if not row:
        # No keyword was found in snippet.
        return "No snippet found"

    return row


def search(word):
    """
    Provide a search facility
    listing snippets which contain a given 'word' strings anywhere in their messages. 
    return the snippet
    """
    with connection, connection.cursor() as cursor:
        cursor.execute("select keyword, message from snippets where not hidden and message like '%%'||%s||'%%'",
                       (word,))
        result = [result for result in cursor.fetchall()]
    logging.debug("Snippet search result retrieved successfully.")
    if not result:
        return "No snippet found"
    return result

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")
    put_parser.add_argument("--hide", help="flag the hidden column True", action="store_true")
    # put_parser.add_argument("--unhide", help="flag the hidden column False", action="store_false") # should be conflicting option...


    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="Name of the snippet")

    # Subparser for the delete command
    logging.debug("Constructing update subparser")
    delete_parser = subparsers.add_parser("delete", help="delete a snippet")
    delete_parser.add_argument("name", help="Name of the snippet")

    # Subparser for the catalog command
    logging.debug("Constructing catalog subparser")
    catalog_parser = subparsers.add_parser("catalog", help="Retrieve a name")

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="search snippets")
    search_parser.add_argument("word", help="search word for the snippet")

    arguments = parser.parse_args()

    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))

    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))

    elif command == "catalog":
        print(catalog())
        print("Retrieved list of names")

    elif command == "delete":
        name = delete(**arguments)
        print("Deleted snippet: {!r}".format(name))

    elif command == "search":
        snippet = search(**arguments)
        print("Retrieved the search result: {!r}:".format(snippet))

if __name__ == "__main__":
    main()
