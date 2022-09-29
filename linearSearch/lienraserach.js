
//  linear search 

// iterate through all of the items in the array then check the codition then when u find the match break from the loop

let allTheValues = ["45", 74, 85, 10, 63 ,"41", true]

var valuesToBeSearched = 85;
var flag = true


for(var i=0; i< allTheValues.length; i++){
    if(allTheValues[i] == valuesToBeSearched){
        console.log("Found At Index ="+ i ) 
        flag = false
        break
    }
}
if(flag){
    console.log("The Item You Looking For Not Found In Here!")
}