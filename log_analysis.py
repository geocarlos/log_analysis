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

get_top_15()
