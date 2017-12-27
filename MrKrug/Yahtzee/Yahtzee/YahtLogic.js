// YahtLogic.js:
var diceTrace = [false, false, false, false, false];
var rollCount = 0;
var wholeScore = 0;

function markScore(x){
    var elt = document.getElementById("scoreTally");
    if(x > 6){
      if(!checkDice(x)) return;
    }
    if(x > 6){
        wholeScore += x;
    } else {
        wholeScore += getNumber(x);
    }
    elt.innerHTML = wholeScore;
}

function fullStraight(){
	vals = [];
	for(var i=1; i < 6; i++){
		vals[i-1] = document.getElementById("spot" + i).innerHTML;
	}
	vals.sort();
	for(var j=0; j < 5; j++){
		if(vals[j] != (j + 1)) return false;
	}
	return true;
}

function fullHouse(){
  var match01 = 1;
  var target01;
  var match02 = 0;
  var target02 = "NOTHING";

  var eltTDj = document.getElementById("spot1");
  target01 = eltTDj.innerHTML;

  for(var j=1; j< 5; j++){
      var eltTDj = document.getElementById("spot" + (j + 1));
      if(target01 == eltTDj.innerHTML){
        match01++;
        continue;
      }
      if((target02 == "NOTHING") || (eltTDj.innerHTML == target02)){
        target02 = eltTDj.innerHTML;
        match02++;
      }
    }
  return (((match01 == 3) && (match02 == 2)) || ((match01 == 2) && (match02 ==3)));
}

function getFace(num){
	var val = [0,0,0,0,0];
	var cnt = [0,0,0,0,0];

	for(var i=1; i < 6; i++){
		var elt = document.getElementById("spot" + i);
		for(var j=1; j<6; j++){
			if(val[j-1] == elt.innerHTML){
				cnt[j-1]++;
			}
		}
	}
	for(var k=0; k < 5; k++){
		if(cnt[k] == nuk){
			return val[k];
		}
	}
return 0;
}

function checkDice(numIn){
    var matchedDice = getMatches();
    if((numIn ==  33) && (matchedDice < 3)){
      alert("Sorry, there is no triplet!");
    } else {
      if(numIn == 33){
        wholeScore += getNumber(getFace(3));
      }
    }

    if((numIn ==  44) && (matchedDice < 4)){
      alert("Sorry, there is no quadruplet!");
    } else {
	if(numIn == 44){
	  wholeScore += getNumber(getFace(4));
	}
    }

    if((numIn ==  55) && (matchedDice < 5)){
      alert("Sorry, there is no yahtzee!");
    } else {
	if(numIn == 55){
	  wholeScore += 50;
	}
    }

    if((numIn ==  25) && (!fullHouse())){
      alert("Sorry, there is no Full House!");
    } else {
	if(numIn == 25){
	  wholeScore += 25;
	}
    }
    alert("Whole Score: " + wholeScore);
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
  alert(mostMatches);
  return mostMatches;
}

function getNumber(x){
  var score = 0;
  for(var i=0; i<5; i++){
    var eltTD = document.getElementById("spot" + (i + 1));
    if(eltTD.innerHTML == x){
      score += x;
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
  wholeScore = 0;
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
