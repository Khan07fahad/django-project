var abc = [];
$("document").ready(function(){

    $("button#addButton").click(function(){
        var options = $("#input").val();
        //alert(options);
        if (options!= ""){
        $("#orderedList").append("<li>" + options + "</li>");
        $("#orderedList li").click(function(){
            abc.push($(this).detach());
            $("button#addAgainButton").click(function(){
            $("#orderedList").append(abc.pop());
            });
        });
        }
    });

});
