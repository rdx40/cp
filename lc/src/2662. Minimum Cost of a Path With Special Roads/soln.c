#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct {
    int cost, x, y;
} Node;

typedef struct {
    Node* data;
    int size;
    int capacity;
} MinHeap;

void swap(Node* a, Node* b) {
    Node tmp = *a;
    *a = *b;
    *b = tmp;
}

void heapifyUp(MinHeap* heap, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap->data[p].cost <= heap->data[i].cost) break;
        swap(&heap->data[p], &heap->data[i]);
        i = p;
    }
}

void heapifyDown(MinHeap* heap, int i) {
    int smallest = i;
    while (1) {
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if (l < heap->size && heap->data[l].cost < heap->data[smallest].cost) smallest = l;
        if (r < heap->size && heap->data[r].cost < heap->data[smallest].cost) smallest = r;
        if (smallest == i) break;
        swap(&heap->data[i], &heap->data[smallest]);
        i = smallest;
    }
}

void push(MinHeap* heap, int cost, int x, int y) {
    if (heap->size == heap->capacity) return;
    heap->data[heap->size++] = (Node){cost, x, y};
    heapifyUp(heap, heap->size - 1);
}

Node pop(MinHeap* heap) {
    Node top = heap->data[0];
    heap->data[0] = heap->data[--heap->size];
    heapifyDown(heap, 0);
    return top;
}

int absval(int x) {
    return x < 0 ? -x : x;
}

// Hashmap for visited using linear probing
#define VISITED_SIZE 200003

typedef struct {
    long long key;
    int cost;
} Entry;

Entry visited[VISITED_SIZE];

int getVisited(long long key) {
    int i = key % VISITED_SIZE;
    while (visited[i].key != 0) {
        if (visited[i].key == key) return visited[i].cost;
        i = (i + 1) % VISITED_SIZE;
    }
    return -1;
}

void setVisited(long long key, int cost) {
    int i = key % VISITED_SIZE;
    while (visited[i].key != 0 && visited[i].key != key) {
        i = (i + 1) % VISITED_SIZE;
    }
    visited[i].key = key;
    visited[i].cost = cost;
}

int minimumCost(int* start, int startSize, int* target, int targetSize,
                int** specialRoads, int specialRoadsSize, int* specialRoadsColSize) {

    MinHeap heap;
    heap.size = 0;
    heap.capacity = 100000;
    heap.data = (Node*)malloc(sizeof(Node) * heap.capacity);

    memset(visited, 0, sizeof(visited));

    push(&heap, 0, start[0], start[1]);

    while (heap.size > 0) {
        Node curr = pop(&heap);
        int cost = curr.cost, x = curr.x, y = curr.y;

        long long key = ((long long)x << 32) | (unsigned int)y;
        int prev = getVisited(key);
        if (prev != -1 && prev <= cost) continue;
        setVisited(key, cost);

        if (x == target[0] && y == target[1]) {
            free(heap.data);
            return cost;
        }

        int directCost = cost + absval(target[0] - x) + absval(target[1] - y);
        push(&heap, directCost, target[0], target[1]);

        for (int i = 0; i < specialRoadsSize; ++i) {
            int* road = specialRoads[i];
            int x1 = road[0], y1 = road[1];
            int x2 = road[2], y2 = road[3];
            int c  = road[4];

            int toStart = absval(x1 - x) + absval(y1 - y);
            int totalCost = cost + toStart + c;

            push(&heap, totalCost, x2, y2);
        }
    }

    free(heap.data);
    return -1;
}
