function myFunction(){
    document.getElementById("myForm").reset();
}


function myAnalyser(){
    document.querySelector('.main div').style.display='none';
    document.querySelector('.main').classList.add('spinner-1')
    setTimeout(() => {
        document.querySelector(".main").classList.remove('spinner-1');
        document.querySelector(".main div").style.display='block';

    }, 5000);
}