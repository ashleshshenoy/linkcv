const fileUploader = document.getElementById('preview')
const div = document.createElement('div')
const btn = document.createElement('button');
div.style.cssText =`
backdrop-filter: blur(5px);
width:100%;
position:absolute;
display:flex;
justify-content:center;
align-items:center;
background-color:#f9fafb;
top:0;
height:100%;
width:100%
z-index:2;
`
btn.innerHTML = "View"
btn.style.cssText = `
    color:white;
    background:var(--primary);
    z-index:3  ;

    
`
const container=document.getElementsByClassName('preview-container')[0]
div.append(btn)
container.appendChild(div)

btn.addEventListener('click',() => {
    div.style.display = 'none'
})
