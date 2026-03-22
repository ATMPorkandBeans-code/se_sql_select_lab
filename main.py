# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd
# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# df_answer = pd.read_sql("""SELECT * FROM employees""", conn)

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName
                             FROM employees""", conn)


# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber
                             FROM employees""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS "ID"
                             FROM employees""", conn).head(5)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                        SELECT jobTitle,
                        CASE
                        WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
                        ELSE "Not Executive" 
                        END as role
                        FROM employees""", conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
                            SELECT length(lastName) AS name_length
                             FROM employees""", conn)



# STEP 7
# Replace None with your code
df_short_title =pd.read_sql("""
                            SELECT substr(jobTitle, 1, 2) AS short_title
                             FROM employees""", conn)

# STEP 8
# Replace None with your code


other_variable = pd.read_sql("""
                            SELECT SUM(CAST(round(priceEach * quantityOrdered) AS INTEGER)) AS sum_total_price
                             FROM orderDetails""", conn)

sum_total_price = other_variable['sum_total_price']

# # STEP 9
# Replace None with your code
# df_day_month_year = pd.read_sql("""SELECT orderDate from employees;""", conn) 
# print(df_day_month_year)
# order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
# print(order_details)
conn.close()