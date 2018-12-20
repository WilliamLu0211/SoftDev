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

var studentList = ["adayR", "aschJ", "belkebirI", "chenJ", "chowdhuryJ", "cwalinaP", "gondalA", "guptaS", "hasanA", "johalP", "keriazisD", "liK", "linJ", "linV", "liuA", "luW", "maiJ", "mohriC", "narangA", "ngR", "onishiR", "peciR", "petersT", "rachlevskyM", "wongT", "wuR", "yeJ", "zhangI", "zhaoM", "zhouQ"];

var randomStudent = () => {
  var index = parseInt(Math.random() * studentList.length);
  // console.log(studentList[index]);
  return studentList[index];
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

var printR = () => {
  var x = document.getElementById("-r");
  var val = randomStudent();
  x.innerHTML = val;
  console.log(val);
}

var f = document.getElementById("f");
var g = document.getElementById("g");
var r = document.getElementById("r");

f.addEventListener('click', printF);
g.addEventListener('click', printG);
r.addEventListener('click', printR);
