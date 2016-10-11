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

    new_email = raw_input('Please type an email to insert: ')
    for result in result_list:
        if new_email == result.email:
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

def update():
    query = db.query('select * from phonebook')
    update_name = raw_input("Please enter a contact to update: ")

    result_list = query.namedresult()

    for result in result_list:
        if update_name == result.name:
            new_name = raw_input("Please enter a new name for %s: " % (result.name))
            new_number = raw_input("Please enter a new number: ")
            new_email = raw_input("Please enter a new email: ")
            db.update('phonebook', {'id': result.id, 'name': new_name, 'phone_number': new_number, 'email': new_email})
            phone_book()

    for result in result_list:
        if update_name != result.name:
            add_name = raw_input("Name not found. Add it? (Y or N) ")
            if add_name.upper() == 'Y':
                set_up()
            else:
                phone_book()


def delete_all():
    query = db.query('select * from phonebook')
    result_list = query.namedresult()

    for result in result_list:
        db.delete('phonebook', {'id': result.id})
    db.query("""ALTER SEQUENCE phonebook_id_seq RESTART WITH 1""")

def phone_book():
    print "\n"
    print "Electronic Phone Book"
    print "====================="
    print "1\. Search entries\n"
    print "2\. Set up an entry\n"
    print "3\. Delete an entry\n"
    print "4\. List all entries\n"
    print "5\. Update an entry\n"
    print "6\. Delete All Entries\n"
    print "7\. Exit\n"
    usr_input = int(raw_input("What do you want to do (1-7)? "))
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
        update()
    elif usr_input == 6:
        delete_all()
    elif usr_input == 7:
        print "Pce late cy@"
        sys.exit()
    else:
        print "Invalid option."

    while usr_input != 7:
        phone_book()

phone_book()
