/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    
    struct ListNode *head = malloc(sizeof(struct ListNode));
    struct ListNode *next = malloc(sizeof(struct ListNode));
    if(l1==NULL && l2==NULL) return NULL;
    
     
    if(l1==NULL){
       return l2;
        
    }
    
    if(l2==NULL){
       return l1;
        
    }

        if(l1->val < l2->val){
            head->val = l1->val;
            l1 = l1->next;

        }

        else if (l2->val <= l1->val){
            head->val = l2->val;
            l2 = l2->next;
        }
    
    head->next=next;
    
    while(l1!=NULL && l2!=NULL){
        next->next = malloc(sizeof(struct ListNode));        
        
        if(l1->val < (l2->val)){
            next->val = l1->val;
            l1 = l1->next;
            next=next->next;
        
        
        }

        else{
            next->val = l2->val;
            l2 = l2->next;
            next=next->next;    
            
        }
    }
    
    if(l1==NULL){
        next->val=l2->val;
        next->next=l2->next;
        
    }
    
    if(l2==NULL){
        next->val=l1->val;
        next->next=l1->next;
        
    }
    
    return head;
    
    
    
}
