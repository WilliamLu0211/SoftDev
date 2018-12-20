// NothingWorks - William Lu, Imad Belkebir
// SoftDev1 pd7
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-20 R

var fibonacci = (n) => {
  if (!n)
    return 0;
  if (n == 1)
    return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

var gcd = (a, b) => {
  if (!b)
    return a;
  return gcd(b, a % b); //reverses the order of a and b
}

var printF = () => {
  var x = document.getElementById("-f");
  var val = fibonacci(10);
  x.innerHTML = val;
  console.log(val);
}

var printG = () => {
  var x = document.getElementById("-g");
  var val = gcd(12, 9);
  x.innerHTML = val;
  console.log(val);
}

var h = document.getElementById("h");
var thelist = document.getElementById("thelist");
var fiblist = document.getElementById("fiblist");
var b = document.getElementById("b");
var fb = document.getElementById("fb");
var li = document.getElementsByTagName("li");

// thelist.addEventListener('mouseover', function(){
//   console.log(thelist);
// })

for (var i : li)
  i.addEventListener('mouseover', function(){
    h.innerHTML = i.innerHTML;
  })
