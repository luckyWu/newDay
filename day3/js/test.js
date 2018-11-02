function bind(elem,en,fun) {
	if(elem.addEventListener) {
		elem.addEventListener(en,fun,false); 
	} else {
		elem.attachEvent("on"+en,fun); 
	}
}

function unbind(elem,en,fun) {
	if(elem.removeEventListener) {
		elem.removeEventListener(en,fun);
	} else {
		elem.detachEvent("on"+en,fun); 
	}
}
function randomColor(){
	var red = parseInt(Math.random()*256)
	var green = parseInt(Math.random()*256)
	var blue = parseInt(Math.random()*256)
	return "rgb(" + red + "," + green + "," + blue + ")"  ; 
}
function $1(id)
{
	return document.getElementById(id)
}
