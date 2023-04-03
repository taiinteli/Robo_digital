
async function dados(){
    
    let posicaoX = document.querySelector('#posicaox').value;
    let posicaoY = document.querySelector('#posicaoy').value;
    let posicaoZ = document.querySelector('#posicaoz').value;

    const response= await fetch(`http://127.0.0.1:5000/movimentar/${posicaoX}/${posicaoY}/${posicaoZ}`, {
        method: "POST"
    })

    console.log(response)

}