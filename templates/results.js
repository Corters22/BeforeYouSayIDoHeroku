$(document).ready(function(){
    var answers = [];

    $("#next").click(function(){
        $("#page1").hide();
        $("#header").attr('style','margin-top: 50px;')
        $("#page2").removeAttr('style');
        $("#btnSubmit").removeAttr('style');
    });
    $("#btnSubmit").click(function(){
        answers = [];
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

        answers.push($("#sel1").val());
        answers.push($("#sel2").val());
        answers.push($("#sel3").val());
        answers.push($("#sel4").val());
        answers.push($("#sel5").val());
        answers.push($("#sel6").val());
        answers.push($("#sel7").val());
        answers.push($("#sel8").val());
        answers.push($("#sel9").val());
        answers.push($("#sel10").val());

        console.log(answers)
    });
});