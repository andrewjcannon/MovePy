function startup(){
	$("[name='my-checkbox']").bootstrapSwitch();
}

function addElement(parentId, elementTag, elementId, html) {
    // Adds an element to the document
    var p = document.getElementById(parentId);
    var newElement = document.createElement(elementTag);
    newElement.setAttribute('id', elementId);
    newElement.innerHTML = html;
    p.appendChild(newElement);
}

function removeRule(num){
	var row = document.getElementById("row" + num);
	row.parentNode.removeChild(row);
}

function addRule(length){
	var num = length + 1;
	var num = document.getElementById("thetable").rows.length;
	var html = '<td><input name="ext' + num + '" type="text"/></td><td><input name="rule' + num + '" type="text"/></td>' + '<td><button class="btn btn-link" onclick="removeRule(' + num + ')">Remove</button></td>';
	addElement('ruletable', 'tr', 'row' + num, html);
}