
// linear serach using java 


public class linearsearch{

    

    public static void main(String args[]){
        // values to be Initalized
        int values[] = {5,6,4,8,78,96,16,412};
        
        int valueToBeSearched = 96;

        // flag 
        boolean flag = true;

        for(int i=0; i<values.length; i++){
           if(values[i] == valueToBeSearched){
             flag = false; // we have the serached item
             System.out.println("Item = "+values[i]+" Found at Index of :"+i);
           }
        }

        if(flag){
            System.out.println("THE ITEM YOU lOOKING FOR IS NOT IN THE LIST");
        }
    }
}