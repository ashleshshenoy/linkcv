const linkContainer = document.getElementById('link-container')

linkContainer.addEventListener('click',()=>{
    const url = linkContainer.getAttribute('data-url')
    navigator.clipboard.writeText(url)
})


function message(message){
    const div = document.createElement('div')
    div.style.cssText = `
        position: absolute;
        top:10px;
        right:10px;
        width:400px;
        height:40px;
        background-color:yellow;
        border-left:10px solid black;
        border-right:10px solid black;
        display:flex;
        justify-content: center;
        align-items:center;
    

    `
    div.innerHTML = message
    document.body.appendChild(div)
    setTimeout(()=>{
        div.style.display = 'none';
    },2000)
}