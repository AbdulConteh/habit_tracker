var table=document.querySelector('table')

FLASK_APP_API_KEY = process.env.FLASK_APP_API_KEY
require('dotenv').config();


async function getBMI() {
    var response = await fetch(process.env.FLASK_APP_API_KEY, options);
    var fitnessData = await response.json();
    var row=document.createElement('tr')
    var data=document.createElement('td')
    row.append(response)
    return fitnessData;
}
console.log(getFitnessData());

function minimize() {
    document.getElementById("api_data").style.display = "none";
}

function show() {
    document.getElementById("api_data").style.display = "block";
}