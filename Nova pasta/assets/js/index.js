const elementoNome = document.getElementById('nome')
const elementosSituacao = document.querySelector('#situacao')
const elementoImg = document.querySelector('#imagem')
let elementoBtn = document.querySelector('#alterar')

elementoBtn.addEventListener('click',()=>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/armandot.jpg'
        elementoNome.innerText == 'Pernalonga'
        elementosSituacao.innerText = 'Pilantra'
        elementoBtn.value = 'segundo'  }
        else if(elementoBtn.value == 'segundo') { 
            elementoImg.src = './assets/img/entediado.jpg'
            elementoNome.innerText = 'Pernalonga'
            elementosSituacao.innerText = 'Entediado'
            elementoBtn.value = 'terceiro'
        } else if(elementoBtn.value == 'terceiro'){
            elementoImg.src = './assets/img/sofrdor.png'
            elementoNome.innerText = 'Pernalonga'
            elementosSituacao.innerText = 'Arrastando o chifre do asfalto'
            elementoBtn.value = 'quarto'
        } else {
            elementoImg.src = './assets/img/sorrindo.png'
            elementoNome.innerText = 'Pernalonga'
            elementosSituacao.innerText = 'Pensando em cenoura'
            elementoBtn.value = 'primeiro'
        }
})