
//  insertion sort
//  its by checking and swapping the adjacent elements 
// first iterate throught the elements 
//  then check whether the adjacent one is lesser then swap then repeat all the steps



let items = [18,-32,-11,6,68,20,-34]


for(i=0; i < items.length; i++){


    
    var temp = items[i]

    for(j= i-1; i>=0 && items[j] > temp; j--){
        items[j+1] = items[j]
    }

    items[j+1] = temp
}

console.log(items)