//Banana Team
//Cathy Cai, Daniel Gelfand
//SoftDev1 pd6
//K29 -- Sequential Progression II: Electric Boogaloo
//2018-12-20 R



//Return the nth fibonacci number
var fibb = function(n){

    // base case 0
    if(n == 0){
	     return 0;
    }

    // base case 1
    else if (n == 1){
	     return 1;
    }

    // add prev two
    else{
	     return fibb(n -1) + fibb(n -2);
    }

};

//Returns the greatest common divisor of two numbers a and b
var gcd = function (a,b) {

    // this means the previous modulo was 0, so a divided into b
    if (b == 0) {
	     return a
    }

    // finds the smallest interval between the two numbers,
    // if that interval fully divides into b, that is the gcd
    else {
	     return gcd(b, a % b)
    }

}

var stulist = ["james", "tyler", "lauren", "becky", "oliver", "frank"];

//Returns a random student from stulist
var randstu = function(){

    // random num in range
    var num = Math.floor(Math.random() * stulist.length);

    // index that
    return stulist[num];
}

// retrieving elements by their id names

var fibbut = document.getElementById("fib");
var gcdbut = document.getElementById("gcd");
var randbut = document.getElementById("rand");

// defining functions related to that element

//Display fibonacci numbers in console and in the page
var fibdis = function() {
  console.log('fib')
  console.log(fibb(7));
  console.log(fibb(6));
  document.getElementById("p0").innerHTML = fibb(7);
  // document.getElementById("p0").innerHTML = fibb(6);
};

//Display gcd in console and in the page
var gcddis = function() {
  console.log('gcd')
  console.log(gcd(5, 25));
  console.log(gcd(21, 14));
  document.getElementById("p1").innerHTML = gcd(5, 25);
  // document.getElementById("p1").innerHTML = gcd(21, 14);
};

//Display random student in console and in the page
var randdis = function() {
  console.log('random student')
  console.log(randstu());
  console.log(randstu());
  document.getElementById("p2").innerHTML = randstu();
  // document.getElementById("p2").innerHTML = randstu();
};

// calling those functions when button is clicked

fibbut.addEventListener('click', fibdis)
gcdbut.addEventListener('click', gcddis)
randbut.addEventListener('click', randdis)
