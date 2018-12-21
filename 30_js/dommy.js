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

var studentList = ["adayR", "aschJ", "belkebirI", "chenJ", "chowdhuryJ", "cwalinaP", "gondalA", "guptaS", "hasanA", "johalP", "keriazisD", "liK", "linJ", "linV", "liuA", "luW", "maiJ", "mohriC", "narangA", "ngR", "onishiR", "peciR", "petersT", "rachlevskyM", "wongT", "wuR", "yeJ", "zhangI", "zhaoM", "zhouQ"];

var randomStudent = () => {
  var index = parseInt(Math.random() * studentList.length);
  // console.log(studentList[index]);
  return studentList[index];
}

var h = document.getElementById("h");
var thelist = document.getElementById("thelist");
var fiblist = document.getElementById("fiblist");
var studentlist = document.getElementById("studentlist");
var b = document.getElementById("b");
var fb = document.getElementById("fb");
var sb = document.getElementById("sb");
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
  fiblist.appendChild(newElem);
})

sb.addEventListener('click', function(){
  var newElem = document.createElement("li");
  newElem.innerHTML = randomStudent();
  studentlist.appendChild(newElem);
})
