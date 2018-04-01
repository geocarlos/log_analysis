import psycopg2

DBNAME = "news"

def get_top_15():
  """Initial function for testing. Return 20 logs for test."""
  conn = psycopg2.connect(database=DBNAME)
  c = conn.cursor()
  c.execute("select path, count(path) as num from log where path != '/' group by path order by num desc limit 15;")
  info = c.fetchall()
  conn.close()
  return info

def get_top_articles():
    return "This should be the top three articles."

def get_top_authors():
    return "This should be the top article authors"

def get_error_days():
    return "This should be the days with more than 1% requests leading to error"

for info in get_top_15():
    print(info)

print(get_top_articles())
print(get_top_authors())
print(get_error_days())
