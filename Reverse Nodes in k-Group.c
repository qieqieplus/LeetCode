/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if(head == NULL)
        return head;

    const int MAX = 8192; //length of linked list
    int i = 0, len = 0;
    struct ListNode *ptrArr[MAX], *pre, *cur = (struct ListNode *)malloc(sizeof(struct ListNode));
    while (head) {
        ptrArr[len++] = head;
        head = head->next;
    }
    int tail = len - len%k;
    while(i < tail){
        if ((i+1) % k == 0){
            for (int j=0; j<k; j++){
                pre = cur;
                pre->next = cur = ptrArr[i-j];
            }
        }
        i++;
    }
    if(tail < len){
        cur->next = ptrArr[tail];
    }else{
        cur->next = NULL;
    }
    free(cur);
    if(len < k){
        return ptrArr[0];
    }
    else{
        return ptrArr[k-1];
    }
}
