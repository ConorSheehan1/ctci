// Given a binary search tree, design an algorithm which creates a linked list of all the
//nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).
//binary search tree implemented in Q4_1

import java.util.ArrayList;
import java.util.Arrays;

class BS4<T> extends BinarySearchTree<T>{
    public ArrayList<ArrayList<TreeNode<T>>> listOfNodesAtDepth(){
        ArrayList<ArrayList<TreeNode<T>>> answer = new ArrayList<>();

        ArrayList<TreeNode<T>> visited = new ArrayList<>();
        // add root to initial list
        visited.add(this.root);
        int counter = 0;

        while(true){
            //copy visited into answer
            answer.add(new ArrayList<>(visited));

            // create empty toVisit arraylist
            ArrayList<TreeNode<T>> toVisit = new ArrayList<>();

            while(visited.size() > 0){

                //add children to toVisit
                TreeNode<T> current = visited.remove(0);
                if (current.leftChild != null) toVisit.add(current.leftChild);
                if (current.rightChild != null) toVisit.add(current.rightChild);
            }

            // if no more nodes left to visit, exit loop
            if (toVisit.size() < 1){
                break;
            }
            visited = new ArrayList<>(toVisit);

        }
        return answer;

    }
}

public class Question4_4{
    public static void main(String[] args) {
        BS4<Integer> b = new BS4<>();
        //int[] a = {5,4,6,3,5,10};
        int[] a = {10,3,15,1,5,12,20,-1,2,4,6,11,13,17,30};
        for (int i: a){
            b.add(i);
        }

        for (ArrayList<TreeNode<Integer>> list :b.listOfNodesAtDepth()){
            System.out.println(list);
        }

    }
}