

// selection sort

// selection sort

// it works with searching the smallest values 
// has basic items that are current_item and current_minimum
// so u need 2 loops the first will go on over the main loop
// the second one finds the smallest one


let item= [12, 6,-5, 8, 10, 20, -2]

var currentItem  = 0
var currentMinimum = 0

var temp = 0


for( i=0; i < item.length; i++){
    
    currentMinimum = i

    for( j = i+1; j < item.length; j++){
        if(item[j] < item[currentMinimum]){
            currentMinimum = j
        }
    }


    if (i != currentMinimum){

        
    temp = currentItem[i]
    item[i] =  item[currentMinimum]
    item[currentMinimum] = temp


    }

}

item.forEach(element => {
    console.log(element)
});
console.log("element")
function selectionSort(yourArray){
    let arrSize = yourArray.length;
        let currentMin;
    for (i=0; i < arrSize; i++){
    //set minimum to this position
            currentMin = i;
    //check the rest of the array to see if anything is smaller
            for (j=i+1; j < arrSize; j++){
                if (yourArray[j] < yourArray[currentMin]){
                    currentMin = j;
                }
            }
    //if the minimum isn't in the position, swap it
            if (i != currentMin){
                   var temp = yourArray[i];
                    yourArray[i] = yourArray[currentMin];
                    yourArray[currentMin] = temp;
              
            }
        }
    return yourArray;
    }

is = selectionSort(item)

is.forEach(element => {
    console.log(element)
});