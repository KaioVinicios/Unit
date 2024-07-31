var numeroSecreto = Math.floor(Math.random() * 100) + 1;

function enviar() {
    var palpite = document.getElementById("palpite").value;
    if (palpite == numeroSecreto) {
        document.getElementById("mensagem").innerHTML = "Acertou, Parabéns!"
    }
    else if (palpite < numeroSecreto) {
        document.getElementById("mensagem").innerHTML = "Seu palpite é MENOR que o número secreto, tente novamente."
    }
    else {
        document.getElementById("mensagem").innerHTML = "Seu palpite é MAIOR que o número secreto, tente novamente."
    }
}

document.getElementById("enviar").addEventListener("click", enviar);