


def create_record (name, tel, address):
    """"Create record"""
    record = {
        'name' : name,
        'phone' : tel,
        'address' : address
    }
    return record


user1 = create_record("Vasia", "+712345678", "KZ")
user2 = create_record("Petia", "+787654321", "RU")

print (user1)
print (user2)

def give_award(medal, *persons):
    """Gicve persons"""
    for person in persons:
        print ("MR " + person.title() + " award " + medal)


give_award("MSK", "Vasia", "Petia")
give_award("SPB", "Alex", "Petia")
give_award("BRN", "Vasia", "Vova")