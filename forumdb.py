# "Database code" for the DB Forum.

import psycopg2,bleach

DBNAME = 'forum'

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database = DBNAME)
  c = db.cursor()
  query = "select content, time from posts order by time desc"
  c.excute(query)
  posts = c.fetchall()
  db.close()
  
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database = DBNAME)
  c = db.cursor()
  query = "insert into posts values (%s)", (bleach.clean(content),)
  c.excute(query)
  db.commit()
  db.close()



