/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int i = 0; const int MAX = 32;
    struct ListNode* ptrArr[MAX];
    struct ListNode* cur = head;

    while (cur) {
        ptrArr[i++] = cur;
        cur = cur->next;
    }

    int index = i - n;
    head = ptrArr[0];

    if (index <= 0) {
        head = ptrArr[index]->next;
    }else if (index + 1 >= i) {
        ptrArr[index -1]->next = NULL;
    }else {
        ptrArr[index -1]->next = ptrArr[index +1];
    }
    free(ptrArr[index]);
    return head;
}
