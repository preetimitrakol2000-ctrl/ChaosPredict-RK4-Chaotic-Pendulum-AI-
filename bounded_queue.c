#include <stdio.h>
#include <stdlib.h>

#define CAPACITY 5

typedef struct {
    double data[CAPACITY];
    int head;
    int tail;
    int size;
} CircularQueue;

// Initializes the ring buffer in memory
void init_queue(CircularQueue* q) {
    q->head = 0;
    q->tail = -1;
    q->size = 0;
}

// Enqueues a new coordinate point, automatically dropping the oldest element if full
void enqueue(CircularQueue* q, double val) {
    q->tail = (q->tail + 1) % CAPACITY;
    q->data[q->tail] = val;
    
    if (q->size < CAPACITY) {
        q->size++;
    } else {
        // Queue is full; advance head pointer to drop oldest data point
        q->head = (q->head + 1) % CAPACITY;
    }
}

// Flattens the circular layout back into a sequential array for Python handling
void structural_flatten(CircularQueue* q, double* out_array) {
    int curr = q->head;
    for (int i = 0; i < q->size; i++) {
        out_array[i] = q->data[curr];
        curr = (curr + 1) % CAPACITY;
    }
}
