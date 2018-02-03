/*$("document").ready(function(){
    $("button").click(function(){
        var options = $("#input").val();
        //alert(options);
        $("#orderedList").append("<li>" + options + "</li>");
    });
});
*/
function prepareEventHandlers() {
	var button1 = document.getElementById("newButton");
	button1.onclick =  function () {
		var value = document.getElementById("input").value;
        var newElement = document.createElement("li");
        var text = document.createTextNode(value);
        newElement.appendChild(text);
        var element = document.getElementById("orderedList");
        element.appendChild(newElement);
	};
}

window.onload = function () {
	// prep anything we need to
	prepareEventHandlers();
};
