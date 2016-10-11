import pg

db = pg.DB(dbname='music_db')

query = db.query('select songwriter.name, count(song.id) from song inner join songwriter on songwriter.id = song.songwriter_id group by songwriter.name;')

result_list = query.namedresult()
for result in result_list:
    print "Artist name: %s" % (result.name)
    print "Number of songs released: %s" % (result.count)
