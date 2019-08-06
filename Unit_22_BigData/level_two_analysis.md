# Sample Analysis of Vine Reviews on Amazon


## PostgreSQL

* Overall, there are 4291 Vine reviews in the data set:

  ![Images/vine01.png](Images/vine01.png)
  
* The mean rating of Vine reviews is 4.07.
  
  ![Images/vine02.png](Images/vine02.png)
  
* The mean rating of non-Vine reviews is 4.06.
  
  ![Images/vine03.png](Images/vine03.png)
  
* When Vine reviews were filtered for reviews with a total of at least twenty votes, at least half of which were marked as helpful, 94 reviews remained.
  
  ![Images/vine04.png](Images/vine04.png)
  
* The filtered data contained 

  ![Images/vine10.png](Images/vine10.png)
  
* After filtering the data, the mean Vine review rating was 4.20.

  ![Images/vine05.png](Images/vine05.png)

* After filtering the data, the mean non-Vine review rating dropped to 3.35.
  
  ![Images/vine06.png](Images/vine06.png)
  
* The standard deviation was calculated using PostgreSQL's `stddev_pop()` function. In Vine reviews, it was found to be 0.98 stars (rounded up, two significant digits).
  
  ![Images/vine07.png](Images/vine07.png)
  
* In non-Vine reviews, the standard deviation was 1.64. In the filtered data set, there is a wider variance among non-Vine reviews.  
  
  ![Images/vine08.png](Images/vine08.png)

* After filtering, 48 out of 94 Vine reviews, or slightly over 50 percent, had a 5-star rating.

  ![Images/vine09.png](Images/vine09.png)

* After filtering, 15663 out of 40471 non-Vine reviews, or about 39 percent, had a 5-star rating.

  ![Images/vine11.png](Images/vine11.png)


## PySpark

* First, the DataFrame was created.

  ```python
  %pyspark
  df = spark.read.option("header", "true").csv("s3a://amazon-reviews-pds/tsv/amazon_reviews_us_Video_Games_v1_00.tsv.gz",  inferSchema=True, sep="\t")
  video_games_df.show(2)
  ```
  
* Next, the data set was filtered for reviews with twenty or more votes, at least half of which were marked helpful.

  ```python
  %pyspark
  df2 = df.select(["star_rating", "helpful_votes", "total_votes", "vine", "verified_purchase"])
  df2.show(10)

  df3 = df2.filter(df2["total_votes"] >= 20)
  df4 = df3.filter(df3["helpful_votes"]/df3["total_votes"] >= 0.5)
  ```
  
* Two new DataFrames were created, one for Vine reviews, and the other for non-Vine reviews, then the `describe()` method was used to extract basic statistical information:

  ```python
  %pyspark
  from pyspark.sql.functions import col, avg
  paid_df = df4.filter(df4['vine']== 'Y')
  unpaid_df = df4.filter(df4['vine']== 'N')

  paid_df.describe().show()
  unpaid_df.describe().show()
  ```
  
* The mean of Vine reviews was 4.20 with a standard deviation of 0.98. The mean of non-Vine reviews was 3.35 with a standard deviation of 1.64, showing greater variance.

  ![Images/vine12.png](Images/vine12.png)
  
* Slightly over 50 percent of Vine reviews had a 5-star rating.

  ```python
  %pyspark
  paid_five_star_number = paid_df[paid_df['star_rating']== 5].count()
  paid_number = paid_df.count()
  percentage_five_star_vine = float(paid_five_star_number) / float(paid_number)
  print(paid_number)
  print(paid_five_star_number)
  print(percentage_five_star_vine)
  ```

  ![Images/vine13.png](Images/vine13.png)
  
* In contrast, about 39 percent of non-Vine reviews had a 5-star rating.

  ```python
  %pyspark
  unpaid_five_star_number = unpaid_df[unpaid_df['star_rating']== 5].count()
  unpaid_number = unpaid_df.count()
  percentage_five_star_non_vine = float(unpaid_five_star_number) / float(unpaid_number)
  print(unpaid_number)
  print(unpaid_five_star_number)
  print(float(unpaid_five_star_number) / float(unpaid_number))
  ```

  ![Images/vine14.png](Images/vine14.png)
