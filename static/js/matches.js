function loadTeams() {
    fetch('http://127.0.0.1:5002/matches')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            console.log(data.nameHomeTeam);

            kelvin = data.weather
            conversor = kelvin - 273.15
            celsius = conversor.toFixed(1)
            document.getElementById('games').innerHTML = `
                                                        <div class="clima">
                                                            <p>Clima em Guaiaquil (Equador)</p>
                                                            <p><strong>${celsius}° Graus Celsius</strong> - ${data.description}</p>
                                                            
                                                        </div>
                                                        <div class="game">
                                                            <div>
                                                                <img src='${data.homeCrest}'>
                                                                <h3>${data.nameHomeTeam}</h3>
                                                                <p>Score: ${data.scoreHomeTeam}</p>
                                                            </div>

                                                            <p class="vs">vs</p>

                                                            <div>
                                                                <img src='${data.awayCrest}'>
                                                                <h3>${data.nameAwayTeam}</h3>
                                                                <p>Score: ${data.scoreAwayTeam}</p>
                                                            </div>
                                                        </div>`
        })
        .catch(error => {
            console.log(error);
        });
}
loadTeams()