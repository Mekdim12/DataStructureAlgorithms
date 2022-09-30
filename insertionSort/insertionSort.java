
//  insertion sort
//  its by checking and swapping the adjacent elements 
// first iterate throught the elements 



public class insertionSort{


    public static void main(String args[]){

        int [] items = {18,-32,-110,6,-68,20,-34};

        for(int i=1; i< items.length; i++){

            int temp = items[i]; 
            int j = i-1;
            for( ; j >= 0 && items[j] > temp; j--){
                items[j+1] = items[j];
            }

            items[j+1] = temp;


        }

        for(int i=0; i< items.length; i++){
           System.out.println(items[i]);
        }
    }


}