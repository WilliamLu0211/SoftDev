// Generals - William Lu, Puneet Johal
// SoftDev1 pd7
// K30 -- Sequential Progression III: Season of the Witch
// 2018-12-21 F

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
var hw = h.innerHTML;
var ctr = 0;

var addFunc = (elem) => {
  elem.addEventListener('mouseover', function(){
    h.innerHTML = this.innerHTML;
  })

  elem.addEventListener('mouseout', function(){
    h.innerHTML = hw;
  })

  elem.addEventListener('click', function(){
    this.remove();
  })
}

for (i = 0; i < li.length; i ++)
  addFunc(li[i]);

b.addEventListener('click', function(){
  var newElem = document.createElement("li");
  newElem.innerHTML = "new item";
  addFunc(newElem);
  thelist.appendChild(newElem);
})

fb.addEventListener('click', function(){
  var newElem = document.createElement("li");
  newElem.innerHTML = fibonacci(ctr);
  ctr ++;
  // addFunc(newElem);
  fiblist.appendChild(newElem);
})
