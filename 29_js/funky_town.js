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
  console.log(fibonacci(10));
}

var printG = () => {
  console.log(gcd(12, 9));
}

var printR = () => {
  console.log(randomStudent());
}

var v1 = document.getElementById("f");
var v2 = document.getElementById("g");
var v3 = document.getElementById("r");

v1.addEventListener('click', printF);
v2.addEventListener('click', printG);
v3.addEventListener('click', printR);
