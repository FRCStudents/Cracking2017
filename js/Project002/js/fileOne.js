
function init(){
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");
  var answer = document.getElementById("cell6");

  fname.innerHTML = "";
  lname.innerHTML = "";
  answer.innerHTML = "";

}
/****
 * @param sep - one character separator
 * This function responds to one of 5 buttons.
 * Each button passes a 1-char value to use as the separator
 ****/
function doit(sep){
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");
  var answer = document.getElementById("cell6");

  var fullName = sep + fname.value + sep + lname.value + sep;
  answer.innerHTML = fullName;
}

function doit2(){
  var stuff = document.getElementById("cell1");
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");
  alert(lname.value);
  stuff.innerHTML = "OOPS!";
  alert(lname.value);
  var answer = document.getElementById("cell6");
  var sep = document.getElementById("sep");

  /****
   * needs some validation
   ****/
  var pattern = /[\& | \# | \@ | \~ | \*]/;
  var fullName = "";

  if(pattern.test(sep.value)){
    fullName = sep.value + fname.value + sep.value + lname.value + sep.value;
  } else {
    fullName = fname.value + " " + lname.value;
    alert("Sorry, there was a serious problem with the separator you chose!");
  }
  answer.innerHTML = fullName;
}

function doit3(){
  var fname = document.getElementById("fname");
  var lname = document.getElementById("lname");
  var answer = document.getElementById("cell6");

  var sepStar = document.getElementById("r*");
  var sepAmp = document.getElementById("r&");
  var sepAt = document.getElementById("r@");
  var sepPound = document.getElementById("r#");
  var sepTilda = document.getElementById("r~");

  var sep = "";

  if(sepStar.checked){
    sep = "*";
  }
  if(sepAmp.checked){
    sep = "&";
  }
  if(sepAt.checked){
    sep = "@";
  }
  if(sepPound.checked){
    sep = "#";
  }
  if(sepTilda.checked){
    sep = "~";
  }

  fullName = sep + fname.value + sep + lname.value + sep;
  answer.innerHTML = fullName;

}
