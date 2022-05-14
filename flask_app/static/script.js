var table=document.querySelector('table')


};

async function getFitnessData() {
    var response = await fetch(, options);
    var fitnessData = await response.json();
    var row=document.createElement('tr')
    var data=document.createElement('td')
    row.append(response)
    return fitnessData;
}
console.log(getFitnessData());

