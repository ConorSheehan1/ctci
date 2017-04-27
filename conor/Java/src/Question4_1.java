import java.util.Random;
class TreeNode<T>{
    T val;
    TreeNode<T> leftChild;
    TreeNode<T> rightChild;

    TreeNode(T value){
        this.val = value;
    }

    @Override
    public String toString(){
        return this.val.toString();
    }
}

class BinarySearchTree<T>{
    TreeNode<T> root;

    BinarySearchTree(T value){
        this.root = new TreeNode<T>(value);
    }

    BinarySearchTree(){
        this.root = null;
    }

//    void add(T value){
//        TreeNode<T> current = this.root;
//        TreeNode<T> newNode = new TreeNode<T>(value);
//        while(true){
//            if (current== null){
//                current = newNode;
//                return;
//            }
//            if(numInserts)
//
//
//        }
//    }

    // this add is binary search tree style
    void add(T value){
        TreeNode<T> current = this.root;
        if (current == null){
            this.root = new TreeNode<T>(value);
            return;
        }
        while(true){

            //1.compareTo(2)
            // if 2 > 1 compareTo returns value > 0
            // if 2 < 1 compareTo returns value < 0
            // if they're compareTo equal returns 0
            if (((Comparable)value).compareTo((Comparable)current.val)>0){
                if (current.rightChild != null){
                    current = current.rightChild;
                }
                else{
                    current.rightChild = new TreeNode<T>(value);
                    break;
                }
            }
            else {
                if (current.leftChild != null){
                    current = current.leftChild;
                }
                else{
                    current.leftChild = new TreeNode<T>(value);
                    break;
                }
            }
        }
    }

    void dfs(TreeNode<T> node){
        if (node != null){
            System.out.println(node.val);
            dfs(node.leftChild);
            dfs(node.rightChild);
        }
    }

    void dfsPrint(){
        TreeNode<T> current = this.root;
        dfs(root);
    }

    boolean isBalanced(){
        return (checkBalance(this.root) != -1);
    }

    int checkBalance(TreeNode<T> current){
        if (current == null){
            return 0;
        }
        int left = checkBalance(current.leftChild);
        if(left == -1) return -1;

        int right = checkBalance(current.rightChild);
        if(right == -1) return -1;

        // if difference in height is greater than 1, tree is unbalanced
        if(Math.abs(left - right) > 1){
            return -1;
        // return height of node
        }else{
            return 1+ Math.max(left, right);
        }
    }
}

public class Question4_1 {
    public static void main(String[] args){
        int limit = 10;
        Random r = new Random();
        BinarySearchTree<Integer> b = new BinarySearchTree<>();

        for(int i=0; i < limit; i++){
            b.add(r.nextInt(10));
        }
        b.dfsPrint();
        System.out.println(b.isBalanced());

        BinarySearchTree<Integer> c = new BinarySearchTree<>(0);
        System.out.println(c.isBalanced());

    }
}
