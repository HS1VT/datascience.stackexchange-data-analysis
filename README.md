# datascience.stackexchange-data-analysis
This repo analyses user data from datascience.stackexchange from 2014 to Sep'2021 and presents various insights on the data.

Tools/technologies used: MapReduce, Apache Hadoop, Amazon EMR, Linux Shell Scripting

The dataset is available at:
https://archive.org/download/stackexchange/datascience.stackexchange.com.7z

Files that we'll need:

Badges.xml  ---
Comments.xml -- 
PostHistory.xml ---
PostLinks.xml ---
Posts.xml ---
Tags.xml ---
Users.xml ---
Votes.xml ---

The problems that we are going to solve are:

Part 1 Document the fields in each file to create a "schema". Find common fields across files? What may be the purpose in doing so? Present your analysis as a nice table. Organize fields so that the common fields come first.

File Name	Field 1	Field 2	Field 3

Part 2 Using simple shell commands, (grep, wc, sort, uniq, awk etc.) count the number of different Badges and the number of users per badge in the Badges.xml file. Prepare the script to run in parallel using Hadoop streaming.

Part 3 Using the Posts.xml file, write Map-Reduce Jobs to create summary tables (plot wherever possible) for the following:

a. Analyze the popularity of tags (how many posts used each of the tags). Note that a post may have multiple tags. Which theoretical distribution does it look like? 

b. Calculate the View Count Distribution (How many posts were viewed a given number of times). Which theoretical distribution does it look like? Can you identify the top 10 most viewed posts on DataScienceExchange? You can also use their website to verify your answers. Please summarize the posts briefly, i.e. what were they about. 

c. Calculate the number of Posts per Hour of the day, for each of the 24 hours. (Tells us how the user activity varies.) What is the ratio of the peak to lowest user activity per hour? Is there an opportunity for Cloud deployment for Stack Exchange? How much can they save by going to cloud?

Part 4 Using the Comments.xml file, write Map-Reduce Jobs to create summary tables (plot wherever possible) for the total Number of Comments and Median of Comment Length by Month from May 2014 to Sep 2021.

Part 5 Using the Users.xml file and PostsHistory.xml, calculate the correlation coefficient of the reputation of the user in Users.xml to the total answers given by the user in PostsHistory.xml file.
