/*
SickBoys - Daniel Gelfand and Joshua Weiner
SoftDev1 pd6
K#30 -- Sequential Progression III: Season of the Witch
2018-12-21 F
*/
var changeHeading = function(e) {
  var h = document.getElementById("h")
  var evType = event.type; //get the type of event
  if(evType == "mouseover"){
    //Change to text of list
    h.innerHTML = this.innerHTML;
  }
  else{
    //Revert to Hello World
    h.innerHTML = "Hello World";
  }
};

//Gets parent and removes the child
var removeItem = function(e) {
  this.parentNode.removeChild(this);
};

var lis = document.getElementsByTagName("li");
//Loop through ordered list
for(var i=0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', changeHeading);
  lis[i].addEventListener('click', removeItem);
};

//Adds item to the list
var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  var text = "WORD"

  item.innerHTML = text;
  list.appendChild( item );
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if(n < 2){
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
};

var n = 0

var addFib = function(e){
  //console.log(e);
  var list = document.getElementById("otherlist");
  var item = document.createElement("li");
  var text = fib(n);
  n+=1;

  item.innerHTML = text;
  list.appendChild( item );

};

//fibonacci numbers through dynamic programming
var fib2 = function(n) {

  //storing results of subproblems
  var result = [0, 1];
  for (var i = 2; i <= n; i++) {
    result.push(result[i-2] + result[i-1]);
  }

  return result[n];

}

var addFib2 = function(e){
  console.log("ADD fib2");
  var list = document.getElementById("otherlist");
  var item = document.createElement("li");
  var text = fib2(n);
  //Increment
  n+=1;

  item.innerHTML = text;
  list.appendChild( item );
};

var i = 1;
var addNat = function(e){
  console.log("ADD Natural number");
  var list = document.getElementById("natlist");
  var item = document.createElement("li");
  var text = i;
  //Increment
  i+=1;

  item.innerHTML = text;
  list.appendChild( item );
};


var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);

var nb = document.getElementById("nb");
nb.addEventListener("click",addNat)
