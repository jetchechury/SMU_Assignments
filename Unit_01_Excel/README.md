# Unit 1 | Assignment - KickStart My Chart

## Background

Over two billion dollars have been raised using the massively successful crowdfunding service, Kickstarter, but not every project has found success. Of the over 300,000 projects launched on Kickstarter, only a third have made it through the funding process with a positive outcome.

Since getting funded on Kickstarter requires meeting or exceeding the project's initial goal, many organizations spend months looking through past projects in an attempt to discover some trick to finding success. For this week's homework, you will organize and analyze a database of four thousand past projects in order to uncover any hidden trends.

## The Process

![Kickstarter Table](Images/FullTable.PNG)

Using the Excel table provided, the data of four thousand pas Kickstarter projects was modified and analyzed in an attempt to uncover some of the market trends.

* Formulas were used to calculate the following information:
  * Percent funded - the amount of money a campaign made towards reaching its intial goal

  * Average donation - the amount each backer for the project paid on average 

  * Category/Sub-Category - the Category and Sub-Category columns were split into two parts

  * Unix timestamps were converted to a normal date 

  * The COUNTIFS() formula, was used to count how many successful, failed, and canceled projects were created with goals within specified ranges. 

  * A mathematic formula, ws used to find the percentage of projects which were successful, failed, or were canceled per goal range.

* The following pivot tables were created:
  * A pivot table that will analyze the initial worksheet to count how many campaigns were "successful," "failed," "cancelled," or are currently "live" per category.

  * A stacked column pivot chart that can be filtered by country based on the table that were created.

  * A pivot table that analyzes the initial sheet to count how many campaigns were "successful," "failed," "cancelled," or are currently "live" per sub-category.

  * A stacked column pivot chart that can be filtered by country and parent-category based on the table that has been created.

  * A pivot table with a column of state, rows of date created conversion, values based on the count of state, and filters based on parent category and years.


## Conclusions

# Successful State
According to the data set, approximately 53.11% of KickStarter campaigns reach a successful state which can be defined as meeting or exceeding the campaigns initial funding goal. (Please refer to the Limitations section of this report for more information regarding this conclusion)

# Funding Goal & Success
The data set shows that as the project funding goal increases the percentage of projects that reach a successful state decrease.  There also appears to be a correlation between the percent of campaigns cancelled and the campaigns funding goal. (Please refer to the Limitations section of this report for more information regarding this conclusion)

![Figure 1: Outcomes Based on Funding Goal](Images/Output_Fig1.PNG)

## Limitations

# Sample Size
The size of the sample examined is 1.33% of the projects launched on KickStarter.  Examining such a small sample size results in a low confidence level.  The sample size of the data examined will also have an effect on the margin of error and power.  For example, KickStarter reports that about one-third of its campaigns reach a successful state.  However, the data set examined shows that approximately half of KickStarter campaigns reach a successful state.

In addition, all of the spotlight campaigns were successful.  This event biases the data.  If the sample included other spotlight campaigns that were not successful, that data would be less biased and could be used as a better predictor.

![Figure 2: State of KickStart Campaigns by Category](Images/Output_Fig2.PNG)
This table reports that 2185 out of the 4114 (53.11%) campaigns in the data set have reached a successful state.

# Unit of Currency
The database reports the dollar amount in the currency of the country in which the KickStarter campaign was launched.  This can be misleading when examining the data set and creating visual representations.  When working with this data set it is important to convert all dollar amounts to the same currency if a comparison will be made.

## Future Explorations

In the future, it may be beneficial to create a scatterplot in order to examine the relationship between the number of backers a KickStarter campaign and the percent of the campaign that was funded.  This information may be helpful in formulating a marketing strategy for the KickStarter campaign.  

In addition to a scatterplot, a pivot table and bar graph to examine the relationship between staff picks and the state of a campaign may also be beneficial in drawing additional conclusions.



