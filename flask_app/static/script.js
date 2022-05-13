const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'fitness-calculator.p.rapidapi.com',
		'X-RapidAPI-Key': 'af83c16a68mshc9761fe920f5cddp1b6238jsnb0e811e7462e'
	}
};

fetch('https://fitness-calculator.p.rapidapi.com/food?foodid=SR25_1_1', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));
