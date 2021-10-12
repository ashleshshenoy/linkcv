const video = document.getElementById('video')
const source = document.getElementById('source')
const videoPlayList = document.getElementsByClassName('video-wrap-container')

for(let videoIter of videoPlayList)
{
    videoIter.addEventListener('click',()=>{
        const url = videoIter.getAttribute('data-url')
        source.setAttribute('src',url);
        video.load();
        video.play();
    })
}


for(let i=0; i<videoPlayList.length; i++)
{
    const url = videoPlayList[i+1].getAttribute('data-url')
    video.onended = ()=>{
    source.setAttribute('src',url);
    video.load();
    video.play();
}
}



// auto play 
const autoPlayBtn = document.getElementsByClassName('auto-play-control-btn')[0]
const autoPlayBtnContainer = document.getElementsByClassName('auto-play')[0]
autoPlayBtnContainer.addEventListener('click',()=>{
    if(autoPlayBtn.style.cssFloat=="left"){
        console.log('done')
        autoPlayBtn.style.cssFloat = "right"
        autoPlayBtnContainer.style.backgroundColor = "#66CD00";
    }
    else{
        autoPlayBtn.style.cssFloat = "left"
        autoPlayBtnContainer.style.backgroundColor = "white";       
    }
})
