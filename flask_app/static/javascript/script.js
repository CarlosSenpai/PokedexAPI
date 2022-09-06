fetch("https://pokeapi.co/api/v2/pokemon/ditto")
    .then(res => res.json())
    .then(res => {
        console.log(res);
        document.querySelector(".wrapper").innerHTML += `<img src=${res.sprites.front_default} class="image">`
    })
    .catch(err => console.log(err))