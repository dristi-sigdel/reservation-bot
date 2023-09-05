hotel_location = {
    'kathmandu', 'chitwan', 'pokhara'
}

hotel_kathmandu = "'Apple Hotel, ktm'\n'Bat Hotel, ktm'\n'Cat Hotel, ktm'\n'Dog Hotel, ktm'"


hotel_chitwan = "'Elephant Hotel, ctwn'\n'Fish Hotel, ctwn'\n'Goat Hotel, ctwn'\n'Horse Hotel, ctwn'"


hotel_pokhara = "'Ink Hotel, pkr'\n'Joker Hotel, pkr'\n'King Hotel, pkr'\n'Lion Hotel, pkr'"


def check_available(location):
    if location in hotel_location:
        if location == 'kathmandu':
            hotels = hotel_kathmandu
        elif location == 'chitwan':
            hotels = hotel_chitwan
        elif location == 'pokhara':
            hotels = hotel_pokhara
    else:
        hotels = False
        

    return hotels

# print(check_available('pokhara'))