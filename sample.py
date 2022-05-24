import phonenumbers
from some import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "ch")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number=phonenumbers.parse(number,"ro")
print(carrier.name_for_number(service_number,"en"))