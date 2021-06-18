$(document).ready(function(){
    var answers = [];

    $("#next").click(function(){
        $("#page1").hide();
        $("#header").attr('style','margin-top: 50px;')
        $("#page2").removeAttr('style');

    });
    $("#cont").click(function(){
        $("#page1").hide();
        $("#page2").hide();
        $("#page3").hide();
        $("#result").hide();
        $("#header").attr('style','visibility: hidden; height: 0px;')
        $("#page4").removeAttr('style');
        $('#contTable').removeAttr('style');

    });
    $("#btnSubmit").click(function(){
        var answers = {};
        if ($("#sel1").val() == '') {
            alert('Please select a value from the drop down for question 1.');
            return;
        }
        if ($("#sel2").val() == '') {
            alert('Please select a value from the drop down for question 2.');
            return;
        }
        if ($("#sel3").val() == '') {
            alert('Please select a value from the drop down for question 3.');
            return;
        }
        if ($("#sel4").val() == '') {
            alert('Please select a value from the drop down for question 4.');
            return;
        }
        if ($("#sel5").val() == '') {
            alert('Please select a value from the drop down for question 5.');
            return;
        }
        if ($("#sel6").val() == '') {
            alert('Please select a value from the drop down for question 6.');
            return;
        }
        if ($("#sel7").val() == '') {
            alert('Please select a value from the drop down for question 7.');
            return;
        }
        if ($("#sel8").val() == '') {
            alert('Please select a value from the drop down for question 8.');
            return;
        }
        if ($("#sel9").val() == '') {
            alert('Please select a value from the drop down for question 9.');
            return;
        }
        if ($("#sel10").val() == '') {
            alert('Please select a value from the drop down for question 10.');
            return;
        }


        answers['Q40'] = parseInt($("#sel1").val())
        answers['Q38'] = parseInt($("#sel2").val())
        answers['Q12'] = parseInt($("#sel3").val())
        answers['Q19'] = parseInt($("#sel4").val())
        answers['Q16'] = parseInt($("#sel5").val())
        answers['Q18'] = parseInt($("#sel6").val())
        answers['Q20'] = parseInt($("#sel7").val())
        answers['Q15'] = parseInt($("#sel8").val())
        answers['Q9'] = parseInt($("#sel9").val())
        answers['Q36'] = parseInt($("#sel10").val())
       
        function make_prediction(answers){
            d3.json('/prediction', {
                method:'POST', 
                body:JSON.stringify(answers),
                headers: {"Content-type": "application/json; charset=UTF-8"}
            }).then((data) => {
                var gif_url = data;
                console.log(gif_url)
                $("#result").attr('src', gif_url);
                $("#page2").attr('style', 'visibility:hidden;height:0;');
                $("#btnSubmit").attr('style', 'visibility:hidden');
                $("#page3").removeAttr('style');
                
            })    
            
        }    
        make_prediction(answers);
    });
    
        
    });


