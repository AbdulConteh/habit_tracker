var table=document.querySelector('table')

// async function getBMI() {
//     var response = await fetch(, options);
//     var fitnessData = await response.json();
//     var row=document.createElement('tr')
//     var data=document.createElement('td')
//     row.append(response)
//     return fitnessData;
// }
// console.log(getFitnessData());
function minimize() {
    document.getElementById("api_data").style.display = "none";
}

function show() {
    document.getElementById("api_data").style.display = "block";
}