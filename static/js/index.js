function loadTeams() {
    fetch('http://127.0.0.1:5002/nba')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            console.log(data.teamName);

            console.log(data);
            console.log(data.teamName);
            document.getElementById('teams').innerHTML = `
                                                        <div class="team" style="background-color:#${data.color}">
                                                            <img src="${data.foto}">
                                                            <div class="info">
                                                                <h3>${data.teamName}</h3>
                                                                <p><span>Abreviação do time:</span> ${data.abbreviation}</p>
                                                                <p><span>Localizado em:</span> ${data.location}</p>
                                                                <div>
                                                                    <p><span>Veja mais informações em:</span> </p>
                                                                    <a href="${data.url}">www.nba.com</a>
                                                                </div>
                                                            </div>
                                                        </div>`

        })
        .catch(error => {
            console.log(error);
        });
}
loadTeams()