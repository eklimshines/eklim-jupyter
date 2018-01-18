import happybase

def connect_to_ma_database():
    connection = happybase.Connection(host='192.168.201.162', port=9090)
    connection.open()
    return connection

def query_ma_database(table):
    connection = connect_to_ma_database()
    mbr_table = connection.table(table)
    count = 0
    for row in mbr_table.scan(include_timestamp=True):
        count += 1
    print count
    connection.close()

def clear_ma_mbr_database_table():
    connection = connect_to_ma_database()
    mbr_table = connection.table('MisbehaviorReports')
    for row in mbr_table.scan():
        mbr_table.delete(row[0])
    print "MA misbehavior report table has been cleared"

