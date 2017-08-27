mport psycopg2, bleach

def connect():
        return psycopg2.connect("dbname = tournament")

def deleteMatches():
        db = connect()
        c= db.cursor()
        c.execute("update playerStandings set wins = 0")
        c.execute("update playerStandings set matches  = 0")
        db.commit()
        db.close()

def deletePlayers():
        db = connect()
        c = db.cursor()
        c.execute("TRUNCATE TABLE playerStandings RESTART IDENTITY")
        db.commit()
        db.close()

def countPlayers():
        db = connect()
        c = db.cursor()
        c.execute("select count(*)from playerStandings")
        num = c.fetchone()
        db.close()
        return num[0]
def registerPlayer(name):
        db = connect()
        c = db.cursor()
        c.execute("insert into playerStandings (name) values (%s)",(bleach.clean(name),))
        db.commit()
        db.close()
def playerStandings():
        db = connect()
        c = db.cursor()
        c.execute("select * from playerStandings order by wins desc")
        results = c.fetchall()
        db.close()
        return results

def reportMatch(winner, loser):
        db = connect()
        c = db.cursor()
        c.execute("update playerStandings set matches = matches +1 where id = '%s'" % winner)
        c.execute("update playerStandings set matches = matches +1 where id = '%s'" % loser)
        c.execute("update playerStandings set wins = wins +1 where id  = '%s'" % winner)
        db.commit()
        db.close()

def swissPairings():
        pairs = []
        standings = playerStandings()
        for i in range(0, len(standings)-1,2):
                pairs.append(standings[i][:2] + standings[i+1][:2])
        return pairs
