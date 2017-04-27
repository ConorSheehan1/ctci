import com.sun.org.apache.xpath.internal.SourceTree;
import sun.reflect.generics.tree.Tree;
//Given a sorted (increasing order) array, write an algorithm to create a binary tree with
//minimal height.

import java.util.*;
import java.lang.Math;

class BinaryTree<T>{
    TreeNode<T> root;
    int height = 0;
    int numberOfNodes = 0;

    boolean add_heldper(TreeNode<T> start, TreeNode<T> newNode){
        if (start == null){
            this.root = newNode;
            return true;
        }

        if (start.leftChild != null){
            start.leftChild = newNode;
            return true;
        }

        if (start.rightChild != null){
            start.rightChild = newNode;
            return true;
        }
        return false;
    }

    void add(T value){
        // use array list as queue (BFS)
        ArrayList<TreeNode<T>> arr = new ArrayList<>();
        arr.add(this.root);
        TreeNode<T> newNode = new TreeNode<T>(value);

        while (arr.size() > 0){
            TreeNode<T> current = arr.remove(0);

            // break if node has been successfully added
            if (add_heldper(current, newNode)){
                numberOfNodes++;
                break;
            }

            arr.add(current.leftChild);
            arr.add(current.rightChild);
        }

        updateHeight();
    }

    void updateHeight(){
        // log2(numberOfNodes)+1 = height
        // up to 1 nodes is height 1
        // up to 3 nodes is height 2
        // up to 7 nodes is height 3 etc
        // up to 63 nodes is height 6
        this.height = (int)(Math.log10(this.numberOfNodes)/Math.log10(2)) + 1;
    }


}


public class Question4_3 {
    public static void main(String[] args) {
        BinaryTree<Integer> tree = new BinaryTree<>();
        ArrayList<Integer> arr = new ArrayList<>();
        Random r = new Random();


        for(int i=0; i < 63; i++){
            arr.add(r.nextInt(10));
        }

        Collections.sort(arr);
//        while(arr.size() > 0){
//            int middle = arr.size()/2;
//            tree.add(arr.remove(middle));
//        }

        // doesn't specify binary search tree, so no need to worry about order
        for(Integer val: arr){
            tree.add(val);
        }

        System.out.println(tree.height);
    }
}
