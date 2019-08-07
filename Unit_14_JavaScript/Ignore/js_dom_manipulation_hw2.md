# Unit 14 | Assignment - JavaScript and DOM Manipulation

## Lesson 1 - notes and guides

The whats and whys of JavaScript  
**Execution Context and it's importance to understanding JavaScript**  
[Execution Context](https://tylermcginnis.com/ultimate-guide-to-execution-contexts-hoisting-scopes-and-closures-in-javascript/)  
**Need help visualizing where you are in your JavaScript Code**  
[JavaScript Visualizer](https://tylermcginnis.com/javascript-visualizer/)  
**ORDER MATTERS**  
When more than 1 external script file is referenced in HTML file Document, if an variable that is declared in one JavaScript file is used inside of another the file where it is declared must come first!

* Activities and there meaning  
    __*1. Activity 1 Running JavaScript*__
        Review various logging/user input (alerts, console.log, prompts confirms)  
        **additional resources**  
        For the start of class we are rendering responses back to console.log().  
        Primary reason when coding in js is to debug how we are interacting with the DOM.  
        print out a message to a web browser's built-in console  

        script tag along with scr attribute  
        JavaScript code is placed between a pair of script tags inside of the HTML file.  
        when there is an external JavaScript file we would use src attribute to refer to an external JavaScript file.  

    __*2. Activity 2 Python vs JavaScript*__  
        Comparison vs Python  
        variable declaration (var,let, const) - only review var  
        Spelling matters  
        Python f string verse JS `Hello ${name}!`
        JavaScript curly brackets define block of code  
**additional resources**  
[Article 1 diff between var, let, const](https://medium.com/javascript-scene/javascript-es6-var-let-or-const-ba58b8dcde75)  
        **I found this article to be a little more helpful**  
[Article 2 diff between var, let, const](https://tylermcginnis.com/var-let-const/)  

    __*3. Activity 3 JavaScript Loan Approver*__  
        Logical path and nested if's
    __*4. Activity 4 JavaScript Arrays*__  
        JS arrays indexed like python arrays, and can hold multiple arrays.  
        __Python methods__  
        .append() - add to list  
        .join() - joins items into single string  
        .split() - split string into list  

        __JavaScript methods__  
        .push() - add to array
        .pop() - remove item from end of array
        .join() - joins items into single string  
        .split() - split string into list  
        .slice() - return slice of array  
        **additional info**  
[ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)  
    __*5. Activity 5 For Loops*__
        based on acitivity  
        var students = ["Johnny","Tyler","Bodhi","Pappas"]  
        for(var i = 0, i < students.length; i++)
        i contol number of loops  
        i < 10 control stop of loop  
        i ++ (or --) increment or decrement value i at end of each loop
    __*6. Movie Scores*__
        Example of loop
        .length() count items in list
    __*7. Activity 7 Functions*__
        Python functions declared with  
            def addition(a,b):
                return a + b
        JavaScript Functions declared
            function addition(a, b) {
                return a + b;
            }
        Arrays can be passed to JavaScript functions
        Functions can call other JavaScript function
    __*8. Activity 8 Statistics Functions*__
        Practice of writing statistical functions  
        There are stat libraries that can be leveraged look into!  

## Lesson 2 Objects, ES6, and Tables  
Covers following (building blocks for homework):  

* forEach - used extensively in homework  
* call back functions - used extensively in homework
* .map() method
* .filter()
* arrow functions - short cut for inline functions
* basic table structure - manipulate using Bootstrap / HTML

__*Activity 1 forEach & Callback functions*__  
        Comparison of of for loop compared to forEach loop  
        for loop repeat until specific condition met  
        var i = 0; __i < 10__; i ++  
        forEach will using __callback function__ for each element (this is also where you can use inline function - 
        see activity 9 for more info)  
        create function first
        function printName(name) {
          console.log(name);
        }
        using forEach call back function to loop  
        students.forEach(printName);  
        
__*Activity 2 Movie Scores*__  
        practice forEach, call back functions (inline functions)  
        comparable from last lesson.  Variable holding rating scores no longer needed  
        __Old Code__
        // Use a for loop to iterate through the movie scores  
        for (var i = 0; i < movieScores.length; i++) {  

          // Add each score to the ratings count  
          var score = movieScores[i];  
          totalmovie += score;  
        __New Code__  
        movieScores.forEach(function(score) {  
          // Add each score to the ratings count  
          sum += score;  

__*Activity 3 JavaScript Objects (like Python Dictionaries)*__  
    
        __organize__ key & value pairings
        __unorderded__ unlike lists  
        keys __access__ the value  
        Can use both *dot* notation and *bracket* notation but *dot* notation preferred.
        *take away will see again in activity 7* Built in methods to manipulate object.  
        Object.keys()  - in python dict.keys()  
        Object.values() - in python dict.values()  
        Object.entries() - in python dict.items()  

__*Activity 4 Word Frequency Counter*__  
        creating JavaScript object Count word.  Using function for loop count words in string  

__*Activity 5 Map*__
        using .map() with inline function.  .map() creates new array from existing array (like list comprehension 
        in python)  
        xyz.map(function(item, index){
            return `Stage ${index}:${item}`;
            })
        Biggest difference between forEach & Map  
        * forEach executes a function on each element in an array  
        * map creates a new array w/ results calling function on each element in the original array  
[Map vs forEach](https://codeburst.io/javascript-map-vs-foreach-f38111822c0f)
        
__*Activity 6 Arrow Functions (short hand inline functions)*__  
    arrow functions allow to drop word function keyword and only show parameters.
    old way
    var scores = students.map(function(student) {
      return student.score;
        });
    new way
    var mapArrow3 = theStagesOfJS.map(item => item);
    
    item to the left of arrow => name function parameter; and item to right of => is the returned value.
    curly brackets only used when function of body has more lines of code than just returned statement.
    
__*Activity 7 Object Iteration*__ (can be used as a basic example for homework still building block though)  
    using forEach() method in conjunction with Object.keys() iterate through keys of object
    Arrays of objects can use combination of forEach() first iterate through array of objects & then iterate 
    through keys & values of each single object.
    
__*Activity 8 Recipe Iteration*__  
    practice forEach, arrow functions, & Objects().  See BONUS code building array of values using map / arrow
    very clean and simple but takes two passes (ie situational as to when would use)
    
__*Activity 9 Filter*__ (important for this weeks homework.  very basic but important concept)  
    .filter() method creates array filled w/ all array elements that pass a test (a function provided)
    .filter() does not execute function for array elements w/o values
    .filter() does not change orginal array
    
__*Activity 10 Student Filter*__  
        using .filter() method two part process
        1) function named madeCut()
        2) function called by .filter()

__*Activity 11 HTML Tables*__ (important to understand how to manipulate tables built on lesson 
                                    3 used in homework!)  
        table - tags
        each row - tr tags
        header rows - special th tags
        td tags define table cells
        * nesting important always have td w/in rows (tr).  
[Bootstrap Tables Documentation](https://getbootstrap.com/docs/3.3/css/#tables)

## Lesson 3 JavaScript w/ D3.js
    D3 manipulate DOM - will pick back up in week 16
    IMPORTANT CONCEPTS
    DOM manipulation & event handling - will not be covering Data Binding will come in week 16
    * populate table using static data structures
    * understand events
    * use "this" reference elements.  [this link](https://www.w3schools.com/js/js_this.asp) - used in level 2 hw
    * attach events to DOM elements
    * Dynamically manipulate DOM through events
    * Dynamically filter tables

__*Activity 1 Intro to D3 & Select*__  
        similar to selecting DOM with soup.find() 
        learn how to import D3 in script tag using CDN link (Content Delivery Network)
        * d3.select() reference element
        * how to select and change element
        * how to capture attribute with attr() method and access href directly
        * use selectAll() method to select all elements with certain tags, class or id's
        * how to select first element and append child element
        
__*Activity 2 DB Select*__
    manipulate table element adding bootstrap styling - dynamically add row data
    * bonus basic example of what will be doing in homework.  using forEach loop through array dynamically build table
    arrays can be destructed in javascript assignment
    * Arrays can be [destructured](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) in JavaScript assignments. This is similar to unpacking a tuple in Python.
    
__*Activity 3 D3 Table*__ THIS IS KEY PART OF HOMEWORK  
        refactored code to use arrow functions.
        
        data.forEach((weatherReport) => {
          var row = tbody.append("tr");
          Object.entries(weatherReport).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
          });
        });
     
__*Activity 4 D3 Event Listeners*__   
    

        
        
        
        


## Background

WAKE UP SHEEPLE! The extra-terrestrial menace has come to Earth and we here at `ALIENS-R-REAL` have collected all of the eye-witness reports we could to prove it! All we need to do now is put this information online for the world to see and then the matter will finally be put to rest.

There is just one tiny problem though... our collection is too large to search through manually. Even our most dedicated followers are complaining that they are having trouble locating specific reports in this mess.

That's why we are hiring you. We need you to write code that will create a table dynamically based upon a [dataset we provide](StarterCode/static/js/data.js). We also need to allow our users to filter the table data for specific values. There's a catch though... we only use pure JavaScript, HTML, and CSS, and D3.js on our web pages. They are the only coding languages which can be trusted.

You can handle this... right? The planet Earth needs to know what we have found!

## Your Task

### Level 1: Automatic Table and Date Search

* Create a basic HTML web page or use the [index.html](StarterCode/index.html) file provided (we recommend building your own custom page!).

* Using the UFO dataset provided in the form of an array of JavaScript objects, write code that appends a table to your web page and then adds new rows of data for each UFO sighting.

  * Make sure you have a column for `date/time`, `city`, `state`, `country`, `shape`, and `comment` at the very least.

* Use a date form in your HTML document and write JavaScript code that will listen for events and search through the `date/time` column to find rows that match user input.

### Level 2: Multiple Search Categories (Optional)

* Complete all of Level 1 criteria.

* Using multiple `input` tags and/or select dropdowns, write JavaScript code so the user can to set multiple filters and search for UFO sightings using the following criteria based on the table columns:

  1. `date/time`
  2. `city`
  3. `state`
  4. `country`
  5. `shape`

- - -

### Dataset

* [UFO Sightings Data](StarterCode/static/js/data.js)

- - -

**Good luck!**

- - -

### Copyright

Data Boot Camp © 2018. All Rights Reserved.
