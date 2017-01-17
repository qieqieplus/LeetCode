#include <iostream>

struct binaryTree {
    int value;
    binaryTree *left;
    binaryTree *right;
};

int main(){
    binaryTree *ptr = (binaryTree *)malloc(3* sizeof(binaryTree));
    binaryTree *head, *l1, *r1;
    head = ptr;
    head->value = 123;
    l1 = ptr++;
    r1 = ptr++;
    r1->value = 789;
    l1->value = 234;
    head->left = l1;
    head->right = r1        ;

    std::cout<< head->right->value <<std::endl;
    return 0;
}