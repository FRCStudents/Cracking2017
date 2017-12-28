// YahtLogic.js:
var diceTrace = [false, false, false, false, false];
var rollCount = 0;
var wholeScore = 0;

/*
 * this function is fired after the user clicks on
 * the possible score.
 * @haveInfo - true if i have enough info to determine score
 *           - false if I still need to determine what was rolled
 *
 */
function markScore(boxNumber, x, haveInfo, numOfAKind){
    var elt = document.getElementById("scoreTally");
    var score = 0;
    if(!haveInfo){
      //
      // In these cases I still need to determine which die
      // is being used - for example - 3 of a kind could be
      // 3 ones, or 3 fours and I don't know if i am checking
      // for which face
      //
      // checkDice updates wholeScore...
      if(!checkDice(x, numOfAKind, boxNumber)) return;
    }
    // only short and long straights...
    if(x > 6){
        score = scoreStraightSize(getStraightSize());
    } else {
        //getNumber adds up all the x's and returns that score
        // e.g. 3 rolled fives: then getNumber(5) returns 15
        score = getNumber(x);
        //alert("markScore (after getNumber(" + x + ")" + score);
    }
    if(score > 0){
      wholeScore += score;
      //alert("wholeScore after adding score: " + wholeScore);
      elt.innerHTML = wholeScore;
    }
    turnBoxOff(boxNumber);
}

function turnBoxOff(boxNumber){
  eltB = document.getElementById("box" + boxNumber);
  eltB.setAttribute("bgcolor", "black");
}

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

function _fullStraight(){
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

//
// getFace - checks the dice to see how many matching
//            dice there are
// @param num: the number of matches we are looking for
// @return val[k]: the value of the face that matches num times
//      if there is no match - return 0
// e.g. if we have 3 fours:
//    x = getFace(3)
//    getFace returns a 4 to x
//
function getFace(num){
  //alert("getFace(num): " + num);
	var val = [0,0,0,0,0];
	var cnt = [0,0,0,0,0];
//
// for each die
//  get face value
//    count the number of times that face value shows
//    log the face value with the number of times
//
	for(var i=1; i < 6; i++){
		var elt = document.getElementById("spot" + i);
    var faceValue = elt.innerHTML;
    var count = 0;

		for(var j=1; j<6; j++){
      var elt2 = document.getElementById("spot" + j);
			if(faceValue == elt2.innerHTML){
				count++;
			}
		}
    val[i] = elt.innerHTML;
    cnt[i] = count;
	}

	for(var k=0; k < 5; k++){
		if(cnt[k] == num){
			return val[k];
		}
	}
return 0;
}

//
// checkDice does all the heavy lifting
// @param numIn - determines what the user thinks s/he has
// @param numOfAKind - number of matches we are searching for
// @param boxNumber - menu choice - to turn it off...
// @side-effect - updates wholeScore
//
function checkDice(numIn, numOfAKind, boxNumber){
    alert("Begin checkDice: " + wholeScore);
    var elt = document.getElementById("scoreTally");
    var matchedDice = getMatches();
    if((numOfAKind ==  3) && (matchedDice < 3)){
      turnBoxOff(boxNumber);
      alert("Sorry, there is no triplet!");
      return false;
    } else {
      if(numOfAKind == 3){
        wholeScore += getNumber(getFace(numOfAKind));
      }
    }

    if((numOfAKind ==  4) && (matchedDice < 4)){
      turnBoxOff(boxNumber);
      alert("Sorry, there is no quadruplet!");
      return false;
    } else {
    	if(numOfAKind == 4){
    	  wholeScore += getNumber(getFace(numOfAKind));
    	}
    }

    if((numOfAKind ==  5) && (matchedDice < 5)){
      turnBoxOff(boxNumber);
      alert("Sorry, there is no yahtzee!");
      return false;
    } else {
    	if(numOfAKind == 5){
        // yahtzee - score = 50!
        var s = getNumber(getFace(numOfAKind));
        if(s > 0)
    	     wholeScore += 50;
    	}
    }

    if((numIn ==  25) && (!fullHouse())){
      turnBoxOff(boxNumber);
      alert("Sorry, there is no Full House!");
      return false;
    } else {
    	if(numIn == 25){
    	  wholeScore += 25;
    	}
    }
    alert("end checkDice: " + wholeScore);
    elt.innerHTML = wholeScore;
    turnBoxOff(boxNumber);
    return true;
    //alert("[checkDice(): Whole Score: ]" + wholeScore);
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
