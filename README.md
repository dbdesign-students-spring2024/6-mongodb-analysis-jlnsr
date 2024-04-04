# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

## AirBnB [Listings](./data/listings.csv) (ORIGINAL dataset) In The City Of Newark, Essex County, NJ in CSV Format.
## [MUNGED DATASET](./data/listings_clean.csv)

## Sample From the listings.csv    
| id | last_scraped | source | name | description | host_id | host_name | host_since | host_location | host_is_superhost | host_listings_count | host_total_listings_count | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | property_type | room_type | accommodates| bathrooms | bathrooms_text | bedrooms | beds | price | calendar_updated | has_availability | calendar_last_scraped |
 | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- | :-----| :----- | :----- | :----- | :----- | :----- | :----- | :----- | :----- |
62033 | 2023-12-30 | city scrape | Home in Newark · ★4.86 · 1 bedroom · 1 bed · 1 bath |  | 301435 | Fred | 2010-11-27 | Newark, NJ | f | 1 | 1 | Newark | North |  | Private room in home | Private room | 1 |  | 1 bath |  | 1 | $80.00 |  | t | 2023-12-30 |
1975091 | 2023-12-31 | city scrape | Home in Newark · ★4.70 · 1 bedroom · 1 bed · 1 shared bath |  | 9169027 | Kimberly B | 2013-10-01 | Newark | f | 5 | 8 | Newark | West |  | Private room in home | Private room | 2 |  | 1 shared bath |  | 1 | $50.00 |  | t | 2023-12-31 |
2159185 | 2023-12-31 | city scrape | Home in Newark · ★4.87 · 1 bedroom · 1 bed · 1 shared bath |  | 9169027 | Kimberly B | 2013-10-01 | Newark | f | 5 | 8 |  | West |  | Private room in home | Private room | 1 |  | 1 shared bath |  | 1 | $48.00 |  | t | 2023-12-31 |
2277901 | 2023-12-31 | city scrape | Home in Maplewood · ★4.67 · 1 bedroom · 1 bed · 1 private bath |  | 11308972 | Tendai D | 2014-01-14 | Maplewood | t | 4 | 10 | Maplewood | West |  | Private room in home | Private room | 2 |  | 1 private bath |  | 1 | $75.00 |  | t | 2023-12-31 |
2279324 | 2023-12-31 | city scrape | Rental unit in Maplewood · ★4.54 · 1 bedroom · 3 beds · 1 bath |  | 11308972 | Tendai D | 2014-01-14 | Maplewood | t | 4 | 10 | Maplewood | West |  | Entire rental unit | Entire home/apt | 4 |  | 1 bath |  | 3 | $90.00 |  | t | 2023-12-31 |
2695185 | 2023-12-31 | city scrape | Home in Newark · ★4.77 · 1 bedroom · 2 beds · 1 private bath |  | 9169027 | Kimberly B | 2013-10-01 | Newark | f | 5 | 8 | Newark | West |  | Private room in home | Private room | 2 |  | 1 private bath |  | 2 | $62.00 |  | t | 2023-12-31 |
2927685 | 2023-12-31 | city scrape | Home in Newark · ★4.85 · 1 bedroom · 2 beds · 1 shared bath |  | 9169027 | Kimberly B | 2013-10-01 | Newark | f | 5 | 8 | Newark | West |  | Private room in home | Private room | 2 |  | 1 shared bath |  | 2 | $48.00 |  | t | 2023-12-31 |
3319300 | 2023-12-30 | city scrape | Rental unit in Newark · ★4.59 · 1 bedroom · 1 bed · 1 bath |  | 2034171 | David | 2012-03-29 | New York | f | 1 | 1 | Newark | North |  | Entire rental unit | Entire home/apt | 2 |  | 1 bath |  | 1 | $72.00 |  | t | 2023-12-30 |
4007546 | 2023-12-30 | city scrape | Rental unit in Newark · ★4.97 · 1 bedroom · 1 bed · 1 private bath |  | 2734824 | Lei | 2012-06-25 | Newark | t | 1 | 1 | Newark | East |  | Private room in rental unit | Private room | 2 |  | 1 private bath |  | 1 | $67.00 |  | t | 2023-12-30 |
4015993 | 2023-12-30 | city scrape | Home in Newark · ★4.96 · 1 bedroom · 1 bed · 1 private bath |  | 20822869 | Tom | 2014-09-01 | Newark | t | 1 | 1 | Newark | North |  | Private room in home | Private room | 1 |  | 1 private bath |  | 1 | $82.00 |  | t | 2023-12-30 |
4408881 | 2023-12-30 | city scrape | Rental unit in Newark · ★4.82 · 1 bedroom · 1 bed · 1 bath |  | 296707902 | Sergio | 2019-09-21 |  | f | 1 | 1 | Newark | North |  | Entire rental unit | Entire home/apt | 2 |  | 1 bath |  | 1 | $70.00 |  | t | 2023-12-30 |
5459428 | 2024-01-01 | city scrape | Home in Newark · ★4.77 · 1 bedroom · 1 bed · 1 shared bath |  | 9169027 | Kimberly B | 2013-10-01 | Newark | f | 5 | 8 | Newark | West |  | Private room in home | Private room | 2 |  | 1 shared bath |  | 1 | $39.00 |  | t | 2024-01-01 |
6134188 | 2023-12-31 | city scrape | Home in Newark · ★4.98 · 4 bedrooms · 4 beds · 4 baths |  | 26222479 | Caro-Lina | 2015-01-16 | Hilton Head Island | f | 2 | 2 | Newark | North |  | Entire home | Entire home/apt | 10 |  | 4 baths |  | 4 | $350.00 |  | t | 2023-12-31 | 
7612811 | 2023-12-31 | city scrape | Home in Newark · ★4.27 · 1 bedroom · 1 bed · 1 shared bath |  | 39925277 | David | 2015-07-29 | Newark | f | 1 | 1 | Newark | West |  | Private room in home | Private room | 2 |  | 1 shared bath |  | 1 | $350.00 |  | t | 2023-12-31 |
8106551 | 2023-12-31 | city scrape | Rental unit in Newark · ★4.53 · 1 bedroom · 3 beds · 1 bath |  | 37522191 | Arica | 2015-07-05 | Newark | f | 1 | 1 | Newark | East |  | Entire rental unit | Entire home/apt | 1 |  | 1 bath |  | 3 | $120.00 |  | t | 2023-12-31 |
8116202 | 2023-12-31 | city scrape | Townhouse in Newark · ★4.74 · 3 bedrooms · 6 beds · 2 baths |  | 23630245 | Bart | 2014-11-11 | Newark | f | 2 | 2 | Newark | East |  | Entire townhouse | Entire home/apt | 4 |  | 2 baths |  | 6 | $100.00 |  | t | 2023-12-31 |
8404849 | 2023-12-31 | city scrape | Guest suite in Newark · ★4.95 · 1 bedroom · 2 beds · 1 bath |  | 23767297 | Sandy & Tone | 2014-11-15 | Newark | f | 1 | 2 | Newark | South |  | Entire guest suite | Entire home/apt | 2 |  | 1 bath |  | 2 | $125.00 |  | t | 2023-12-31 |
8628016 | 2023-12-30 | city scrape | Rental unit in Newark · ★4.86 · 1 bedroom · 1 bed · 1 shared bath |  | 45377447 | Katiuscia & Andre | 2015-09-29 | Newark | f | 1 | 2 | Newark | East |  | Private room in rental unit | Private room | 1 |  | 1 shared bath |  | 1 | $120.00 |  | t | 2023-12-30 |
8713883 | 2023-12-30 | city scrape | Rental unit in Newark · ★4.48 · 1 bedroom · 1 bed · 1 shared bath |  | 43545556 | Leslie | 2015-09-06 | New Jersey | f | 1 | 5 | Newark | East |  | Private room in rental unit | Private room | 1 |  | 1 shared bath |  | 1 | $84.00 |  | t | 2023-12-30 |
8906383 | 2023-12-31 | city scrape | Rental unit in Newark · ★4.81 · 1 bedroom · 2 beds · 1 shared bath |  | 20241104 | Marlene R | 2014-08-18 | Newark | t | 2 | 2 | Newark | East |  | Private room in rental unit | Private room | 3 |  | 1 shared bath |  | 2 | $60.00 |  | t | 2023-12-31 |   
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
db.listings.find({ beds: { $gt: 2 }, neighbourhood: "Maplewood", }, { _id:0, name:1, beds:1, review_scores_rating:1, price:1, }).sort( {review_scores_rating:-1})
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