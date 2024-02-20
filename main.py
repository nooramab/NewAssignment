class Passenger:
  def __init__(self, fname, lname, age, contact, email):
        self._fname = fname
        self._lname = lname
        self._age = age
        self._contact = contact
        self._email = email

    def get_fname(self):
        return self._fname

    def set_fname(self, fname):
        self._fname = fname

    def get_lname(self):
        return self._lname

    def set_lname(self, lname):
        self._lname = lname

    def get_age(self):
        return self._age

    def set_id(self, age):
        self._age = age

    def get_contact(self):
        return self._contact

    def set_contact(self, contact):
        self._contact = contact

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

class Flight:
    def __init__(self, airline, flight_number, departure_time, arrival_time, departure_airport, arrival_airport):
        self._airline = airline
        self._flight_number = flight_number
        self._departure_time = departure_time
        self._arrival_time = arrival_time
        self._departure_airport = departure_airport
        self._arrival_airport = arrival_airport

    def get_airline(self):
        return self._airline

    def set_airline(self, airline):
        self._airline = airline

    def get_flight_number(self):
        return self._flight_number

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def get_departure_time(self):
        return self._departure_time

    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def get_arrival_time(self):
        return self._arrival_time

    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def get_departure_airport(self):
        return self._departure_airport

    def set_departure_airport(self, departure_airport):
        self._departure_airport = departure_airport

    def get_arrival_airport(self):
        return self._arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self._arrival_airport = arrival_airport

class Traveling:
    def __init__(self, travel_date, departure_terminal, arrival_terminal, seat_number, seat_type,
                     boarding_till_time, price):
        self._travel_date = travel_date
        self._departure_terminal = departure_terminal
        self._arrival_terminal = arrival_terminal
        self._seat_number = seat_number
        self._seat_type = seat_type
        self._boarding_till_time = boarding_till_time
        self._price = price

    def get_travel_date(self):
        return self._travel_date

    def set_travel_date(self, travel_date):
        self._travel_date = travel_date

    def get_departure_terminal(self):
        return self._departure_terminal

    def set_departure_terminal(self, departure_terminal):
        self._departure_terminal = departure_terminal

    def get_arrival_terminal(self):
        return self._arrival_terminal

    def set_arrival_terminal(self, arrival_terminal):
        self._arrival_terminal = arrival_terminal

    def get_seat_number(self):
        return self._seat_number

    def set_seat_number(self, seat_number):
        self._seat_number = seat_number

    def get_seat_type(self):
        return self._seat_type

    def set_seat_type(self, seat_type):
        self._seat_type = seat_type

    def get_boarding_till_time(self):
        return self._boarding_till_time

    def set_boarding_till_time(self, boarding_till_time):
        self._boarding_till_time = boarding_till_time

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

class BoardingPass:
    def __init__(self, ticket_id, passenger, flight, traveling, boarding_gate, barcode, baggage):
        self._ticket_id = ticket_id
        self._passenger = passenger
        self._flight = flight
        self._traveling = traveling
        self._boarding_gate = boarding_gate
        self._barcode = barcode
        self._baggage = baggage

    def get_ticket_id(self):
        return self._ticket_id

    def set_ticket_id(self, ticket_id):
        self._ticket_id = ticket_id

    def get_passenger(self):
        return self._passenger

    def set_passenger(self, passenger):
        self._passenger = passenger

    def get_flight(self):
        return self._flight

    def set_flight(self, flight):
        self._flight = flight

    def get_traveling(self):
        return self._traveling

    def set_traveling(self, traveling):
        self._traveling = traveling

    def get_boarding_gate(self):
        return self._boarding_gate

    def set_boarding_gate(self, boarding_gate):
        self._boarding_gate = boarding_gate

    def get_barcode(self):
        return self._barcode

    def set_barcode(self, barcode):
        self._barcode = barcode

    def get_baggage(self):
        return self._baggage

    def set_baggage(self, baggage):
        self._baggage = baggage

# Example: Creating objects and printing a boarding pass
passenger = Passenger("James", "Smith", 30, "123-456-7890", "james.smith@example.com")
flight = Flight("National Airlines", "NA4321", "11:40", "13:30", "Chicago", "New York JFK")
traveling = Traveling("2020-12-06", "Terminal 2", "Terminal 2", "09A", "FIRST CLASS", "11:20", 25000.00)
boarding_pass = BoardingPass("697", passenger, flight, traveling, "Gate 3", "1234567890", "1 checked bag")
# Print boarding pass details
print("Boarding Pass Details:")
print("Ticket ID:", boarding_pass.get_ticket_id())
print("Passenger Name:", boarding_pass.get_passenger().get_fname(), boarding_pass.get_passenger().get_lname())
print("Flight Details:", boarding_pass.get_flight().get_airline(), boarding_pass.get_flight().get_flight_number())
print("Seat Number:", boarding_pass.get_traveling().get_seat_number())
print("Boarding Gate:", boarding_pass.get_boarding_gate())
print("Travelling From:", boarding_pass.get_flight().get_departure_airport())
print("Travelling To:", boarding_pass.get_flight().get_arrival_airport())
print("Arrival Time:", boarding_pass.get_flight().get_arrival_time())
print("Arrival Terminal:", boarding_pass.get_traveling().get_arrival_terminal())
print("Travel Date and Time ", boarding_pass.get_traveling().get_travel_date(), boarding_pass.get_flight().get_departure_time())
print("Seat Number:", boarding_pass.get_traveling().get_seat_number())
print("Borading Till:", boarding_pass.get_traveling().get_boarding_till_time())
