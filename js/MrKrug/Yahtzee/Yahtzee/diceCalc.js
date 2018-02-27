//*************************************
// workhorse functions -
// determining matches and faces...
//*************************************

function scoreStraightSize(size){
  if(size == 4) return 20;
  if(size == 5) return 30;
  return 0;
}

function getStraightSize(){
  var dice = [0,0,0,0,0];
    for(var i = 0; i < 5; i++){
      elt = document.getElementById("spot" + (i+1));
      dice[i] = elt.innerHTML;
    }
    dice.sort();
    count = 1;
    for(var i=0; i < 4; i++){
      if(dice[i] == dice[i+1] - 1){
        count++;
      }
    }
    return count;
}

function getMatches(){
  var mostMatches = 0;
  var matches = 0;
  for(var j=0; j< 5; j++){
    var eltTDj = document.getElementById("spot" + (j + 1));
    for(var i=j; i<5; i++){
      var eltTDi = document.getElementById("spot" + (i + 1));
      if(eltTDi.innerHTML == eltTDj.innerHTML){
        matches++;
      }
    }
    if(matches > mostMatches){
      mostMatches = matches;
    }
    matches = 0;
  }
  //alert("[getMatches()] mostMatches: " + mostMatches);
  return mostMatches;
}

function getNumber(x){
  var score = 0;
  for(var i=0; i<5; i++){
    var eltTD = document.getElementById("spot" + (i + 1));
    if(eltTD.innerHTML == x){
      score += (x * 1);
    }
  }
  return score;
}


function unsetDiceTrace(i){
  diceTrace[i-1] = false;
}

function setDiceTrace(i){
  diceTrace[i-1] = true;
}
