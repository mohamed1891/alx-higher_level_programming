#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Author - Bamidele Adefolaju
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head, *new;

    /* Attempt to allocate memory for the new node */
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    /* Set the number for the new node */
    new->n = number;

    /* If the list is empty or the new number is less than the head, insert at the beginning */
    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return (new);
    }

    /* Traverse the list to find the correct insertion point */
    while (node && node->next && node->next->n < number)
        node = node->next;

    /* Insert the new node */
    new->next = node->next;
    node->next = new;

    /* Return the new node */
    return (new);
}
