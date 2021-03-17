#sudo pip3 install phonenumbers
# keep number in one file
import phonenumbers as pn
# to get variable from on python file in same directory
#from file_name import variable_name_from_file

number="+91----------" #number must include country code

from phonenumbers import geocoder # to get location
ch_number=pn.parse(number,"CH") # number,countrycode as the paramerter

#c - is for country and h- is for history

print(geocoder.description_for_number(ch_number,"en")) #  number and language u want output

# to find service provider

from phonenumbers import carrier
service_number=pn.parse(number,"RO") #
print(carrier.name_for_number(service_number,"en"))
