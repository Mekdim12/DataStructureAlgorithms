

//  binary search 


//  declare all the items
// iterated through the elements 
// first check the middle one if not 
// compare the value with seraching items decide to go right or left
// them continue this step until u found or finish the list len(items) < 2 halt the program



public class binarySearch{

    public static void main(String args[]){
        
        int[] items = {0,4,7,10,14,23,45,47,53};

        int VALUETOBESERACHED = 47;

        int initialIndex = 0;
        int endIndex = (items.length) -1;

        boolean flag = false;

        while(initialIndex <= endIndex){
            
            int indexOfMidValue = (int) (initialIndex + endIndex) / 2;

            if(items[indexOfMidValue] == VALUETOBESERACHED ){
                System.out.println("The Item Found At Index :"+ indexOfMidValue);
                flag = true;
                break;
            }else if( items[indexOfMidValue]  < VALUETOBESERACHED ){
                initialIndex = indexOfMidValue + 1;
                  System.out.println("RIGHT");
          
            }else{
                endIndex = indexOfMidValue - 1;
                  System.out.println("LEFT");
          
            }

        }

        if(!flag){
            System.out.println("THE ITEM YOU LOOKING FOR IS NOT IN THE LIS");
              }

    }
}