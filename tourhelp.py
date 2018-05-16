
import json


#load hotel data from json file

#ask from user and get:
#start and end date of stay
#low and high cost range
#low and high rating range
#number of people


#compare user's inputs with hotel availability
def loadhoteldata():
    with open('hotel.json') as data_file:
        hotel_info = json.load(data_file)
    return hotel_info

def loadtouristdata():
    with open('tourist.json') as data_file:
        tourist_info = json.load(data_file)
    return tourist_info

def touristInput(tourist_info):
    tourist_info["date"]["start_date"] = raw_input("Please insert your starting date: ")
    tourist_info["date"]["end_date"] = raw_input ("Please insert your ending date: ")
    tourist_info["number_people"] = int(raw_input (" Please insert number of people: "))
    tourist_info["rating"]["low"] = int(raw_input("Please insert the lowest rating of the hotel: "))
    tourist_info["rating"]["high"] = int(raw_input("Please insert the highest rating of the hotel: "))
    tourist_info["cost"]["high"]= int(raw_input("Please insert the maximum amount you can pay: "))
    tourist_info["cost"]["low"]= int(raw_input("Please insert the minimum amount you can pay: "))
    tourist_info["location"] = raw_input("Please insert your desired location: ")


    return tourist_info

def compare_json(tourist_info,hotel_info):
    for key in hotel_info:
        if tourist_info["location"]== hotel_info[key]["location"]:
            if tourist_info["rating"]["low"] >= hotel_info[key]["rating"]:
                #print hotel information that matches
                for item in hotel_info[key]["reservation_list"]:
                    print str(tourist_info)
                    print str(hotel_info)
                    if tourist_info["number_people"] <= item["number_of_persons"]:
                        print "There are enough spaces in the room for the number of people you want"
                    else:
                        print "There is not enough space in the room for the number of people you want"
                    if tourist_info["cost"]["high"] > item["payment"]:
                        print " Matched room"
                    else:
                        print "sorry, there isn't any match "
                    if tourist_info["date"]["start_date"] == item["start_date"] and \
                      tourist_info["date"]["end_date"] == item["end_date"]:
                        print "You can reserve in your desired date"
                    else:
                        print "sorry, your desired date has already reserved "





def savetourist(tourist_info):
    print (json.dumps(tourist_info))
    file = open("tourist.json", "w")
    file.write(json.dumps(tourist_info))
    file.close()


def main():
    #call function loading hotel data
    #call function(s) asking user for inputs & storing inputs in json file
    hotel_info = loadhoteldata()
    tourist_info = loadtouristdata()
    tourist_new_info = touristInput(tourist_info)
    tourist_new_info = compare_json(tourist_info, hotel_info)
    savetourist(tourist_new_info)


main()
