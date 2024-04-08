from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == "__main__":
    with create_connection(database) as conn:
        if conn is not None:
            with open("create.sql") as sql:
                sql_queries = sql.read()
                for query in sql_queries.split(";"):
                    create_table(conn, query)
        else:
            print("Error! cannot create the database connection.")
