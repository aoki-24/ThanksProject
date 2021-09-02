

  document.addEventListener('DOMContentLoaded', () => {
    const ballonsection = document.querySelector('.bubble-background');
    const createBallon = () => {
      const img_element  = document.createElement('img');
      img_element.width = 80;
      img_element.height = 100;
      const maxNumber=15
      const minNumber=1
      const number=parseInt(Math.random() * (maxNumber) + minNumber);
      img_element.src = '/static/Grateful_Episode/media/'+number+'.png';
      img_element.className = 'balloon';
      img_element.style.left = Math.random() * innerWidth + 'px';
      ballonsection.appendChild(img_element);
  
      setTimeout(() => {
        img_element.remove();
      }, 8000);
    }
  
    let activeBallon = null;
  
    const stopBalloon = () => {
      clearInterval(activeBallon);
    };
  
    const balloncb = (entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting) {
            activeBallon = setInterval(createBallon, 1600);
        } else {
          stopBalloon();
        }
      })
    };
  
    const ballonoptions = {
      rootMargin: "100px 0px"
    }
  
    const ballonio = new IntersectionObserver(balloncb, ballonoptions);
    ballonio.POLL_INTERVAL = 100; 
    ballonio.observe(ballonsection);
  });