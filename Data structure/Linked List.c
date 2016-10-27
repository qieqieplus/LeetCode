struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* build(int len){
	ListNode *head, *cur, *pre;
	pre = cur = head = (ListNode *)malloc(sizeof(struct ListNode));
	for (int i = 0; i < len; i++){
		cur->val = rand() % (10 * len);
		cur->next = NULL;
		if (i >= 1){
			pre->next = cur;
		}
		pre = cur;
		cur = (ListNode*)malloc(sizeof(struct ListNode));
	}
	return head;
}

void walkthough(struct ListNode* head){
	ListNode* cur = head;
	while (cur) {
		printf("%d\n", cur->val);
		cur = cur->next;
	}
	printf("===============\n");
}