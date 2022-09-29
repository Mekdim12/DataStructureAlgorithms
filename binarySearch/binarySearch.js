

//  binary search 


//  declare all the items
// iterated through the elements 
// first check the middle one if not  if it found its best case scenario so use do while just as precheck before starting the main loop
// compare the value with seraching items decide to go right or left
// them continue this step until u found or finish the list len(items) < 2 halt the program


let items = [0,4,7,10,23,45,47,53]

var valueToBeSearchedFor = 7

var valueFound = false


var initialofItems = 0
var lastOfItems = (items.length) -1 



do{

    var index = parseInt((initialofItems + lastOfItems)/2)

    if (items[index] == valueToBeSearchedFor){
        valueFound = true
        console.log("Values Found At Index : "+ index)
        break;
    }else{

        if(items[index] < valueToBeSearchedFor){
            // 100 < 200  false so we should leave the left section
          
            initialofItems = index +1
            console.log("Right");
        }else{
            // 100 > 45
            //  so we should leave the right section
            lastOfItems = index -1
            console.log("Left");

        }
    }

}while(!valueFound &&  initialofItems <= lastOfItems);
    // while(true && index >= 1); 


if(!valueFound){
    console.log("Values you looking for did not found Here ")
}

