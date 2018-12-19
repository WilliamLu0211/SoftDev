// Generals - William Lu, Puneet Johal
// SoftDev1 pd7
// K28 -- Sequential Progression
// 2018-12-19 W

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
  return studentList[index];
}

var v1 = document.getElementById("1");
v1.addEventListener("click", fibonacci(1));
