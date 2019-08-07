// from data.js
var tableData = data;

var tbody=d3.select("tbody");
buildTable(data);

function buildTable(inpData){
    tbody.html("");
    inpData.forEach(function(ufoSightings){
        var row = tbody.append("tr");

        Object.entries(ufoSightings).forEach(function([key,value]){

            var cell=row.append("td");
            cell.text(value);
        });
    });
}

//Select submit button
var submit=d3.select("#filter-btn");

submit.on("click",function(){

    //Prevent page from refreshing
    d3.event.preventDefault();
    
    //Select date to be used as filter
    var InputElement=d3.select("#datetime");
    var inputDate=InputElement.property("value");

    console.log(inputDate);
    console.log(tableData);


//Find input value for city
    var inputCity=d3.select("#city");
    var cityValue=inputCity.property("value").trim().toLowerCase();


//Find input value for state
    var inputState=d3.select("#state");
    var stateValue=inputState.property("value").trim().toLowerCase();



//Find input value for country
    var inputCountry=d3.select("#country");
    var countryValue=inputCountry.property("value").trim().toLowerCase();


//Find input value for shape
    var inputShape=d3.select("#shape");
    var shapeValue=inputShape.property("value").trim().toLowerCase();

    //Create a custom filtering function based on search criteria entered
    //For each filter option if field is not blank perform filter operation by input value.
    //If no input value data will be equal to data search began with.
    if (inputDate !=""){
        function filterByDate(dateEntry){
            return dateEntry.datetime === inputDate;};

        var filteredByDate=tableData.filter(filterByDate);}

        else {
            var filteredByDate=tableData;
        };
    
    if(cityValue !=""){
        function filterbyCity(cityEntry){
            return cityEntry.city === cityValue.toLowerCase();};

        var filteredByCity=filteredByDate.filter(filterbyCity);}

        else{
            var filteredByCity=filteredByDate;
        };

    if(stateValue !=""){
        function filterbyState(stateEntry){
            return stateEntry.state === stateValue.toLowerCase();};

        var filteredByState=filteredByCity.filter(filterbyState);}

        else{
            var filteredByState=filteredByCity;
        };

    if(countryValue !=""){
        function filterbyCountry(countryEntry){
            return countryEntry.country === countryValue.toLowerCase();};

        var filteredByCountry=filteredByState.filter(filterbyCountry);}

        else{
            var filteredByCountry=filteredByState;
        };
    
    if(shapeValue !=""){
        function filterbyShape(shapeEntry){
            return shapeEntry.shape === shapeValue.toLowerCase();};

        var filteredByShape=filteredByCountry.filter(filterbyShape);}

        else{
            var filteredByShape=filteredByCountry;
        };
 
        
//Print results in console log and build table based on filtered data
    console.log(filteredByShape);
    buildTable(filteredByShape);
});