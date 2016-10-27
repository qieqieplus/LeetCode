/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	struct ListNode *head, *cur;
	if (!l1) return l2;
	if (!l2) return l1;

	if (l1->val <= l2->val){
		head = cur = l1;
		l1 = l1->next;
	}
	else{
		head = cur = l2;
		l2 = l2->next;
	}

	while (l1 || l2){
		if (l1 == NULL){
			cur->next = l2;
			break;
		}
		if (l2 == NULL){
			cur->next = l1;
			break;
		}
		if (l1->val <= l2->val){
			cur->next = l1;
			l1 = l1->next;
		}
		else{
			cur->next = l2;
			l2 = l2->next;
		}
		cur = cur->next;
	}

	return head;
}
