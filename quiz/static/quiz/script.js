var interval_1;
var interval_2;
var counter = 0

document.addEventListener('DOMContentLoaded', () => {

    fetch('display')
    .then(response => {
        return response.json()
    })
    .then(data => {
        const question = data;
        document.querySelector('#question').textContent = question[0].question;
        document.querySelector('#btn1').textContent = question[0].answers[0];
        document.querySelector('#btn1').value = question[0].answers[0];
        document.querySelector('#btn2').textContent = question[0].answers[1];
        document.querySelector('#btn2').value = question[0].answers[1];
        document.querySelector('#btn3').textContent = question[0].answers[2];
        document.querySelector('#btn3').value = question[0].answers[2];
        document.querySelector('#btn4').textContent = question[0].answers[3];
        document.querySelector('#btn4').value = question[0].answers[3];
        document.querySelector("#counter").textContent = counter;            
    })

    
    document.querySelectorAll('button').forEach(function (button) {

        button.onclick = function () {

            clearInterval(interval_1);
            clearInterval(interval_2);
            document.body.style.backgroundColor = "whitesmoke";
            document.querySelector('#time').innerHTML = `<p>&nbsp;</p>`

            interval_2 = setInterval(function(){

                document.body.style.backgroundColor = 'LightYellow';
                document.querySelector('#time').innerHTML = `<p>TIME OUT...</p>`  

            }, 8000)

            

            interval_1 = setInterval(function(){
                         
                fetch('newquestion/wrong')
                .then(response => {
                    return response.json()       
                })
                .then(data => {
                    const question = data;
                    document.querySelector('#question').textContent = question[0].question;
                    document.querySelector('#btn1').textContent = question[0].answers[0];
                    document.querySelector('#btn1').value = question[0].answers[0];
                    document.querySelector('#btn2').textContent = question[0].answers[1];
                    document.querySelector('#btn2').value = question[0].answers[1];
                    document.querySelector('#btn3').textContent = question[0].answers[2];
                    document.querySelector('#btn3').value = question[0].answers[2];
                    document.querySelector('#btn4').textContent = question[0].answers[3];
                    document.querySelector('#btn4').value = question[0].answers[3];
                    counter += 1
                    document.querySelector("#counter").textContent = counter;       
                }).catch(function (error) {
                    console.log(error)
                    window.location.href = 'end'     
                });
            }, 10000);

            fetch(`newquestion/${button.value}`)
            .then(response => {
                return response.json()       
            })
            .then(data => {
                const question = data;
                document.querySelector('#question').textContent = question[0].question;
                document.querySelector('#btn1').textContent = question[0].answers[0];
                document.querySelector('#btn1').value = question[0].answers[0];
                document.querySelector('#btn2').textContent = question[0].answers[1];
                document.querySelector('#btn2').value = question[0].answers[1];
                document.querySelector('#btn3').textContent = question[0].answers[2];
                document.querySelector('#btn3').value = question[0].answers[2];
                document.querySelector('#btn4').textContent = question[0].answers[3];
                document.querySelector('#btn4').value = question[0].answers[3];
                counter += 1
                document.querySelector("#counter").textContent = counter;

            }).catch(function (error) {
                console.log(error)
                window.location.href = 'end'     
            });

        }
        
    });
})

