"""place your code to clean up the data file below."""
#this py program will ommit some of the superflous categories (i.e columns)
#hence perform a reduction of fields
import csv 

with open("data/listings.csv","r") as file:
    #create list of dicts with all fields and data
    all_data = list(csv.DictReader(file))
    
    for record in all_data.copy(): #iterate through shallow copy so changes can be made to the size of the actual object without raising an error
        for field,value in record.items():
            if field in ("listing_url","scrape_id","neighborhood_overview","picture_url","latitude","longitude","amenities","license","instant_bookable"):
                record[field] = "---"
            elif "host" in field:
                if field not in ("host_name","host_id","host_since","host_location","host_is_superhost","host_listings_count","host_total_listings_count"): #i.e. keep all the host related fields we want and scrap the rest
                    record[field] = "---"
                else:
                    if field == "host_location":
                        record[field] = (record[field].split(","))[0]
            elif ("minimum" in field) or ("maximum" in field):
                if (field != "minimum_nights") or (field != "maximum_nights"):
                    record[field] = "---"
            elif "availability" in field:
                if field != "has_availability":
                    record[field] = "---"
            elif "review" in field:
                if (field != "number_of_reviews") or (field != "review_scores_rating"):
                    record[field] = "---"
            elif "calculate" in field:
                record[field] = "---"
            elif field == "neighbourhood":#every entry for neighbourhood consists of three locations, it should only contain the FIRST one (i.e. 'neighbourhood') with no further specifity
                #e.g. "Newark, NJ, United States" should just be "Newark"
                record[field] = (record[field].split(","))[0]

    for record in all_data:
        for field,value in (record.copy()).items():
            if value == "---": #now remove all uneccessary fields
                del record[field]
   
#write the updated dataset to a file named 'listings_clean.csv'
with open("data/listings_clean.csv", "w") as output:
    headers = "" #first line
    for (index,key) in enumerate(list(all_data[1].keys())):
        if index == len(list(all_data[1].keys()))-1:
            headers += (str(key)+"\n")
        else:
            headers += (str(key)+",")
    output.write(headers)
    
    line = ""
    for row in all_data:##fix
        #create a list of all data for each field (of each row) that will dynamically change for each row
        data = list(row.values())
        for (index,value) in enumerate(data):
            if index == len(list(row.values()))-1:
                if value == '': #if there are any fields with an empty String for a value, set that value to "---" so empty values can be parsed correctly when writing to the CSV file
                    line += "---" + "\n"
                else:   
                    line += value + "\n"
            else:
                if value == '':
                    line += "---" + ","
                else:
                    line += value + ","
        output.write(line)
        line = ""
    
    for row in all_data[11:21]:
        for value in row.values():
            print(value+" | ",end="",sep="")
        print()
        print()