let text = document.getElementById("input")
document.addEventListener("keyup",() => {
    aiueo = text.value.length
    p =document.getElementById("count")
    p.textContent = "文字数:"+aiueo
    console.log(text)

    }
)