//*************************************
// dice manipulation -
// working with the images...
// rolling dice...
// turning dice on and off
//*************************************
function turnBoxOff(boxNumber){
  eltB = document.getElementById("box" + boxNumber);
  eltB.setAttribute("bgcolor", "black");
}

function rollDie(){
    return Math.floor((Math.random() * 6) + 1);
}

function roll(){
  rollCount++;
  if(rollCount > 3){
    alert("Too many rolls!");
    return;
  }
  for(var i=0; i<5; i++){
    if(diceTrace[i]) continue;
    var eltTD = document.getElementById("spot" + (i + 1));
    eltTD.innerHTML = rollDie();
  }
}

function firstRoll(){
  rollCount = 0;
  //wholeScore = 0;
  for(var i=0; i<5; i++){
    diceTrace[i] = false;
    var eltTD = document.getElementById("spot" + (i + 1));
    eltTD.innerHTML = "";
    eltTD.setAttribute("bgcolor", "white");
  }
  roll();
}

function solidify(x){
    var eltTD = document.getElementById("spot" + x);
    if(!diceTrace[x - 1]){
      eltTD.setAttribute("bgcolor", "red");
      setDiceTrace(x);
      return;
    }
    eltTD.setAttribute("bgcolor", "pink");
    unsetDiceTrace(x);
}
