import psycopg2

DBNAME = "news"

def get_conn(query):
  """Creates connection to be used in functions to retrieve data."""
  conn = psycopg2.connect(database=DBNAME)
  c = conn.cursor()
  c.execute(query)
  data = c.fetchall()
  conn.close()
  return data

def get_top_articles():
    return get_conn('''select path, count(path) as num from log
    where path != '/'
    group by path
    order by num desc
    limit 3;''')

def get_top_authors():
    return "This should be the top article authors"

def get_error_days():
    return "This should be the days with more than 1% requests leading to error"

print(get_top_articles())
print(get_top_authors())
print(get_error_days())
