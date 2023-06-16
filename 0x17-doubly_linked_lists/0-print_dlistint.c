#include "lists.h"
#include <stdio.h>
#include <stddef.h>
/**
* print_dlistint- print all the element of dlistint
* @h:linked list
*
*Return: The number of node
*/


size_t print_dlistint(const dlistint_t *h);{
    
    int count = 0;

while (h != 0)
{
count++;
h = h->next;
}
return (count);

}