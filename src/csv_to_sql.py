import pandas as pd
import sqlite3

students = pd.read_csv('../data/students.csv')
conn = sqlite3.connect('../data/Students.sqlite')
students.to_sql('Student', conn, if_exists='append', index=False)




