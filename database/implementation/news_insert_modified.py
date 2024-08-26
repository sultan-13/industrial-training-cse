import os
import mysql.connector
from mysql.connector import Error
from db_connection import create_db_connection


def execute_query(connection, query, data=None):
    """
    Execute a given SQL query on the provided database connection.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    query : str
        The SQL query to execute.
    data : tuple, optional
        The data tuple to pass to the query, for parameterized queries.

    Returns
    -------
    None
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_category(connection, name, description):
    """
    Inserts a new category into the categories table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the category.
    description : str
        The description of the category.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    data = (name, description)
    execute_query(connection, query, data)

def insert_reporters(connection, name, email):
    """
    Inserts a new reporter into the reporters table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the reporter.
    email : str
        The email of the reporter.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO reporters (name, email)
    VALUES (%s, %s)
    """
    data = (name, email)
    execute_query(connection, query, data)

def insert_publisher(connection, name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram):
    """
    Inserts a new publisher into the publishers table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    name : str
        The name of the publisher.
    email : str
        The email of the publisher.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO publishers (name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (name, email, phone_number, head_office_address, website, facebook, twitter, linkedin, instagram)
    execute_query(connection, query, data)

def insert_news(connection, category_id, author_id, editor_id, datetime, title, body, link):
    """
    Inserts a new news article into the news table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    category_id : int
        The ID of the category.
    author_id : int
        The ID of the author.
    editor_id : int
        The ID of the editor.
    datetime : datetime
        The publication date and time of the news article.
    title : str
        The title of the news article.
    body : str
        The body text of the news article.
    link : str
        The URL link to the full news article.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO news (category_id, author_id, editor_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, author_id, editor_id, datetime, title, body, link)
    execute_query(connection, query, data)

def insert_image(connection, news_id, image_url):
    """
    Inserts a new image into the images table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the image.
    image_url : str
        The URL of the image.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO images (news_id, image_url)
    VALUES (%s, %s)
    """
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    """
    Inserts a new summary into the summaries table.

    Parameters
    ----------
    connection : mysql.connector.connection.MySQLConnection
        The connection object to the database.
    news_id : int
        The ID of the news article associated with the summary.
    summary_text : str
        The text of the summary.

    Returns
    -------
    None
    """
    query = """
    INSERT INTO summaries (news_id, summary_text)
    VALUES (%s, %s)
    """
    data = (news_id, summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn is not None:
        # insert_category(conn, "Politics", "All news related to politics")
        # insert_reporters(conn, "khaled", "khaled@example.com")
        # Add more insert calls for other tables
        # reporters = [
        #     ("Khaled Ibn Delowar", "khaled@gmail.com"),
        #     ("Jane Smith", "jane@example.com"),
        #     ("Bob Johnson", "bob@example.com")
      
        # ]
        # for reporter in reporters:
        #     insert_reporters(conn, *reporter)
        # publishers_data = [
        #     ("Publisher 1", "publisher1@example.com", "1234567890", "123 Main St", "http://publisher1.com", "publisher1_fb", "publisher1_twitter", "publisher1_linkedin", "publisher1_instagram"),
        #     ("Publisher 2", "publisher2@example.com", "0987654321", "456 Oak St", "http://publisher2.com", "publisher2_fb", "publisher2_twitter", "publisher2_linkedin", "publisher2_instagram"),
            
        # ]
        # for publisher_data in publishers_data:
        #     insert_publisher(conn, *publisher_data)

#         news_data = [
#     (1, 1, 1, "2024-05-16", "News title 1", "Body text for news article 1", "https://example.com/news1"),
#     (2, 1, 2, "2024-05-17", "News title 2", "Body text for news article 2", "https://example.com/news2"),
#     (3, 2, 1, "2024-05-18", "News title 3", "Body text for news article 3", "https://example.com/news3"),
  
# ]
#         for news_item in news_data:
#             insert_news(conn, *news_item)

 
#         images_data = [
#             (1, "https://example.com/image1.jpg"),
#             (2, "https://example.com/image2.jpg"),
#             (3, "https://example.com/image3.jpg"),

#         ]
#         for image_data in images_data:
#             insert_image(conn, *image_data)
        # Example usage to insert multiple summaries
        summaries_data = [
            (1, "Summary text for news article 1"),
            (2, "Summary text for news article 2"),
            (3, "Summary text for news article 3"),
            # Add more tuples as needed
        ]
        for summary_data in summaries_data:
            insert_summary(conn, *summary_data)
