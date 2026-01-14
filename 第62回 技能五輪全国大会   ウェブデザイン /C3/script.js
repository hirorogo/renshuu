function gen() {

    const dives = document.querySelectorAll("div")
    dives.forEach(element => {
        let random = Math.random().toString(16).slice(-6)

        element.style.backgroundColor = "#" + random
        element.innerHTML = ` <span>#${random}</span>`
        element.style.color = `#${random}`
    });
}
gen();