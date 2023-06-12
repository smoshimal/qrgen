import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter your number  :")
phnumber=phonenumbers.parse(number)
timezone=timezone.time_zones_for_number(phnumber)
carrier=carrier.name_for_number(phnumber,'en')
region=geocoder.description_for_number(phnumber,'en')
print(phnumber)
print(timezone)
print(carrier)
print(region)