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

"""
1. What are the most popular three articles of all time?
Which articles have been accessed the most?
"""
def get_top_articles():
    return get_conn('''select a.title, count(a.title)
    as views from articles a, log l
    where path != '/' and a.slug = substr(l.path,10)
    group by a.title
    order by views desc
    limit 3;''')

"""
2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author has written,
which authors get the most page views?
"""
def get_top_authors():
    """
    The query used here depends on a view,
    which has been created with the code below:

    create view authors_views as
    select au.id, count(l.*) as views
    from articles ar, authors au, log l where au.id = ar.author
    and ar.slug =substr(l.path, 10)
    group by au.id, l.path, ar.author;
    """
    return get_conn('''
    select au.name, sum(av.views) as views
    from authors au, authors_views av
    where au.id = av.id group by av.id, au.name
    order by views desc;''')

"""
3. On which days did more than 1% of requests lead to errors?
"""
def get_error_days():
    return get_conn('''select path, count(path) as num from log
    where path != '/'
    group by path
    order by num desc
    limit 3;''')

print("\nTop articles: \n");
for a in get_top_articles():
    print(a[0] + " - " + str(a[1]) + " views")

print("\n\nTop authors: \n");
for a in get_top_authors():
    print(a[0] + " - " + str(a[1]) + " views")
# print(get_error_days())
