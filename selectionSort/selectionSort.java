

//  selection sort using java


public class selectionSort{


    public static void main(String args[]){
            

        int [] items = {12, 6,-5, 8, 10, 20, -2};
        int currentMinimum = 0;
        
        for(int i =0; i < items.length; i++){

            currentMinimum = i;

            for(int j = i+1 ; j < items.length; j++){

                if (items[currentMinimum] > items[j]){
                    
                    currentMinimum = j;
                }

            }

            int temp = items[i];
            items[i] = items[currentMinimum];
            items[currentMinimum] = temp;

        }

    }
}