// YahtLogic.js:
var diceTrace = [false, false, false, false, false];
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
        score = (x == scoreStraightSize(getStraightSize()) ? x : 0);
        //score = scoreStraightSize(getStraightSize());
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
    elt.innerHTML = wholeScore;
    turnBoxOff(boxNumber);
    return true;
}


//////////////////////////////////////////////

function showInstructions(){
  var elt = document.getElementById("animate");
  elt.style.visibility = "hidden";

  var eltI = document.getElementById("instructions");
  eltI.style.visibility = "visible";
  eltI.style.top = '59px';
  eltI.style.left = '359px';

  var pos = 0;
  var height = 25;
  var width = 425;
  var top = 59;
  var left = 359;

  var id = setInterval(frame, 5000);
  function frame() {
    if (pos == 350){
      clearInterval();
      return;
    } else {
      if(pos == 2){
        id = setInterval(frame, 20);
      } else {
        pos+=2;
        top += pos;
        width += pos;
        eltI.style.top = top + 'px';
        eltI.style.left = width + 'px';
        height += 5;
        width += 5;
      }
    }
  }
}
