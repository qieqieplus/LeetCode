struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* build(int len){
    ListNode* head, cur, pre;
    cur = head;
    for (int i=0; i < len; i++){
        cur->val = i+1;
        cur->next = NULL;
        if(i >= 1){
            pre->next = cur;
        }
        pre = cur;
        cur = (ListNode*)malloc(sizeof(ListNode));
    }
    return head;
}

void walkthough(struct ListNode* head){
    ListNode* cur = head;
    while (cur) {
        std::cout << cur->val << std::endl;
        cur = cur->next;
    }
}
