# D3 - Data Journalism

View final product here: https://jetchechury.github.io/SMU_Assignments/Unit_16_D3/

## Background

The objective of this assignment was to analyze the current trends shaping people's lives, as well as creating charts, graphs, and interactive elements to help readers understand the findings. The data set used was based on 2014 ACS 1-year estimates: [https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml). The data set inclded data on rates of income, obesity, poverty, etc. by state.

## The Process

To begin a scatter plot with circle elements to represent each state and axes labels was created between two of the data variables. Code for this graphic can be found in the `app.js` file.  Data was pulled from `data.csv` by using the `d3.csv` function. 

To include more demographics and more risk factors, additional labels were placed in the scatter plot and given click events so that users are able to decide which data to display. The transitions for the circles' locations as well as the range of your axes were also animated. In addition, CSV data was bound to circles and a tooltip was added to allow users to view a specific element's data when the cursor is hovered over teh element.
x
