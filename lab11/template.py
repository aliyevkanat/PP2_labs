import psycopg2 
import csv


# Creating a connection
conn = psycopg2.connect(
    database = 'phonebook',
    user = 'postgres',
    host = 'localhost',
    password = 'Aa1234',
    port = 5432
)

conn.autocommit = True

# Commands

create_function_count_by_year = """
        CREATE OR REPLACE FUNCTION count_with_year(selected_year INTEGER)
        RETURNS INTEGER AS 
        $$ 
        BEGIN 
        RETURN COUNT(*) FROM students WHERE students.year > selected_year;
        END; $$
        LANGUAGE plpgsql;
"""

# create_function_select_by_name = """
#         CREATE OR REPLACE FUNCTION select_name(entered_name VARCHAR)
#         RETURNS TABLE(
#             id integer,
#             name varchar, 
#             telephone varchar,
#             year integer
#         ) AS
#         $$ 
#         BEGIN 
#             RETURN QUERY 
#             SELECT * FROM students WHERE students.name = entered_name;
#         END;
#         $$
#         LANGUAGE plpgsql;
# """

# create_function_select_starts_with = """
#         CREATE OR REPLACE FUNCTION select_starts_with(student_name varchar)
#         RETURNS TABLE(
#             id integer,
#             name varchar,
#             telephone varchar,
#             year integer
#         ) AS 
#         $$
#         BEGIN
#         SELECT s.id, s.name, s.telephone, s.year FROM students s WHERE s.name LIKE student_name || '%';
#         END;
#         $$
#         LANGUAGE plpgsql;
# """

create_func_filter_by_first_letter = """
    CREATE OR REPLACE FUNCTION filter_by_first_letter(letter VARCHAR(1))
    RETURNS TABLE (id INTEGER, name VARCHAR(255), telephone VARCHAR(255), year INTEGER)
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM students WHERE LEFT(students.name, 1) = letter;
    END;
    $$
    LANGUAGE plpgsql;
"""

create_procedure_insert_new = """
        CREATE OR REPLACE PROCEDURE add_new_student(
        new_student_name VARCHAR,
        new_student_telephone varchar, 
        new_student_year integer
        ) 
        AS $$ 
        BEGIN 
        INSERT INTO students(name, telephone, year) 
        VALUES (new_student_name, new_student_telephone, new_student_year);
        END; $$
        LANGUAGE plpgsql;
"""

create_procedure_delete_by_name = """
        CREATE OR REPLACE PROCEDURE delete_student(
        student_name varchar
        )
        AS $$
        BEGIN
        DELETE FROM students WHERE name = student_name;
        END; $$ 
        LANGUAGE plpgsql;
"""



# Functions

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# execute_query(create_function_count_by_year)
# execute_query(create_function_select_starts_with)
# execute_query(create_func_filter_by_first_letter)


# Example function for callproc() function 
def call_function_w_args(function_name, args):
    try:
        with conn.cursor() as cur:
            cur.callproc(function_name, args)
            return cur.fetchall()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Procedures 

# Inserting a new student
def insert_new(student_to_insert):
    command = "CALL add_new_student(%s, %s, %s)"
    try:
        with conn.cursor() as cur:
            cur.execute(command, (student_to_insert))
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Deleting by username 
def delete_by_username(username):
    command = 'CALL delete_student(%s)'
    try:
        with conn.cursor() as cur:
            cur.execute(command, (username,))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


students_to_insert = [
    ('Raim', '7084234234', 2),
    ('Alexandra', '3234234243', 2),
    ('Amanat', '2342342', 2)
]

# Calling functions in python 

# execute_query(create_procedure_insert_new)
# insert_new(students_to_insert[2])

# execute_query(create_procedure_delete_by_name)
# delete_by_username('Amanat')


# Using a function that has a callproc() function 
print(call_function_w_args('filter_by_first_letter', ('S',)))














# select_by_username('Sasuke')
# execute_query(create_function_select_by_name)