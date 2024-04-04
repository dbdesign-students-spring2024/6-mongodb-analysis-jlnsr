# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

## AirBnB [Listings](./data/listings.csv) In The City Of Newark, Essex County, NJ in CSV Format  

## Sample From the listings.csv    
id,last_scraped,source,name,description,host_id,host_name,host_since,host_location,host_is_superhost,host_listings_count,host_total_listings_count,neighbourhood,neighbourhood_cleansed,neighbourhood_group_cleansed,property_type,room_type,accommodates,bathrooms,bathrooms_text,bedrooms,beds,price,calendar_updated,has_availability,calendar_last_scraped
| id | last_scraped | source | name | description | host_id | host_name | host_since | host_location | host_is_superhost | host_listings_count | host_total_listings_count | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | property_type | room_type | accommodates| bathrooms | bathrooms_text | bedrooms | beds | price | calendar_updated | has_availability | calendar_last_scraped |
 | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :-----| :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- |
62033 | 2023-12-30 | city scrape | Home in Newark · ★4.86 · 1 bedroom · 1 bed · 1 bath |  | 301435 | Fred | 2010-11-27 | Newark, NJ | f | 1 | 1 | Newark | North |  | Private room in home | Private room | 1 |  | 1 bath |  | 1 | $80.00 |  | t | 2023-12-30 |    
## Scrubbing Process
I developed a python program, using the csv module, to convert the data into an easily digestable list format, where every row of data was represented by a dictionary of values corresponding to the fields in the actual dataset. In running queries on the original **listings.csv** file, I also notice certain inconsistencies in some of the data cells that had to be fixed for the clarity of the results. For instance, "Newark" is regarded as one neighbourhood; however, there were a few inconsistent varieties of the way the same neighbourhood value was conveyed. Some cells added extra spaces, others differed in the capitalization schema. In order to remedy this, I had to standardize the data in this particular field. Where the neighbourhood was listed along with the state (New Jersey) as well as the country--both completely unneccessary--I updated the values, with python, so that only the neighbourhood as a String would appear. I.e. "Newark , NJ, United States" or "Newark, NJ, United States" was changed to just "Newark","Maplewood","Irvington", etc.
# ANALYSIS(Queries)
### 1. Two documents from the listings collection in any order:
```mongodb
db.listings.find().sort( {price:-1},).limit(2)
```
### 2. 10 documents ordered by **minimum_nights**, ascending, "prettyprinted":
```
db.listings.find().sort({minimum_nights:1}).limit(10).pretty()
```
### 3. Choose two hosts (by reffering to their **host_id** values) who are superhosts (available in the **host_is_superhost field**), and show all of the listings offered by both of the two hosts with only **name**, **price**, **neighbourhood**, **host_name**, and **host_is_superhost** for each result.  
FIRST let’s take a look at all superhosts by entering a query that returns just the **host_id** of all documents that have **host_is_superhost** value of ‘t’;
```
db.listings.find({host_is_superhost:'t'},{_id:0,host_id:1})
```  
NEXT, let’s choose the first two unique **host_id**’s that come up (i.e. **11308972** and **2734824**)   
```
db.listings.find({ $or:[{host_id:11308972},{host_id:2734824},] },{_id:0,name:1,price:1,neighborhood:1,host_name:1,host_is_superhost:1})
```
### 4. Show all the unique **host_name** values
```
db.listings.distinct("host_name")
```
### 5. Find all of the places that have more than 2 beds in a neighborhood of your choice, ordered by **review_scores_rating** descending;  
My original query;
```
db.listings.find({ beds: { $gt: 2 }, neighbourhood: "Maplewood, New Jersey, United States", }, { _id:0, name:1, beds:1, review_scores_rating:1, price:1, }).sort( {review_scores_rating:-1})
```  
only churned one result. So I constructed another query referring to another field (**neighbourhood_cleansed**) holding the value of **“South”** for the sake of producing more results;   
```
db.listings.find({ beds: { $gt: 2 }, neighbourhood_cleansed: "South", }, { _id:0, name:1, beds:1, review_scores_rating:1, price:1, }).sort( {review_scores_rating:-1})
```
### 6. Show the number of listings per host:
```
db.listings.aggregate([
{$group: {_id: "$host_name", numHostListings: {$sum: 1} }}
])
```  
Owing to the number of documents corresponding to each name, this query will not display all the results and instead prompt the user to enter ‘it’ to see more results.
### 7. Find the average **review_scores_rating** per neighborhood, and only show those that are 4 or above, sorted in descending order of rating:  
FIRST create a variable **avgRating** that will store a query that will compute the average rating for each neighbourhood:
```
let avgRating = {
$group: {
    _id:"$neighbourhood",
    avgRating: {$avg: "$review_scores_rating"},
    },
}
```    
THEN create a variable **fourAndAbove** that will store a query that will display ONLY the neighborhoods with a rating equal to or greater than 4.  
```
let fourAndAbove = {
    $match: {
    avgRating: {$gte:4},
    },
}
```    
THEN perform an aggregation pipeline with the previously defined variables, sorting the result by average rating in descending order:  
```
db.listings.aggregate([avgRating,fourAndAbove]).sort({avgRating:-1})
```