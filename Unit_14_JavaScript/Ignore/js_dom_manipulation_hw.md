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
        **additional info** [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
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
