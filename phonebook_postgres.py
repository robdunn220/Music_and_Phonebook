import pg
import sys

db = pg.DB(dbname='phonebook')

def search():
    search_name = raw_input('Please type a name to search: ')
    query = db.query('select * from phonebook')

    result_list = query.namedresult()

    for result in result_list:
        if search_name == result.name:
            print "Name: %s" % (result.name)
            print "Number: %s" % (result.phone_number)
            print "Email: %s" % (result.email)

def set_up():
    new_name = raw_input('Please type a name to insert: ')
    query = db.query('select * from phonebook')
    result_list = query.namedresult()

    for result in result_list:
        if new_name == result.name:
            print "Name already exists."
            print "Back to menu"
            phone_book()

    new_number = raw_input('Please type a number to insert: ')
    for result in result_list:
        if new_name == result.name:
            print "Name already exists."
            print "Back to menu"
            phone_book()

    new_email = raw_input('Please type an email to insert: ')
    for result in result_list:
        if new_name == result.name:
            print "Name already exists."
            print "Back to menu"
            phone_book()

    db.insert('phonebook', name= new_name, phone_number= new_number, email= new_email)
    print "Name: %s" % (new_name)

    phone_book()

def delete():
    delete_name = raw_input("Please enter a contact to delete: ")
    query = db.query('select * from phonebook')

    result_list = query.namedresult()

    for result in result_list:
        if delete_name == result.name:
            db.delete('phonebook', {'id': result.id})

def list_all():
    query = db.query('select * from phonebook')
    print query

def phone_book():
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Search entries\n"
    print "2\. Set up an entry\n"
    print "3\. Delete an entry\n"
    print "4\. List all entries\n"
    print "5\.Exit\n"
    usr_input = int(raw_input("What do you want to do (1-6)? "))
    print "\n"

    if usr_input == 1:
        search()
    elif usr_input == 2:
        set_up()
    elif usr_input == 3:
        delete()
    elif usr_input == 4:
        list_all()
    elif usr_input == 5:
        sys.exit()

    while usr_input != 5:
        phone_book()

phone_book()
