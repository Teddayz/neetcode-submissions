class LRUCache {

    HashMap<Integer, Node> hashMap;
    int capacity;
    Node head;
    Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head = new Node(0, 0, null, null);
        this.tail = new Node(0, 0, null, null);
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.hashMap = new HashMap<>();
    }
    
    public int get(int key) {
        if (this.hashMap.containsKey(key)) {
            Node node = this.hashMap.get(key);
            deleteNode(node);
            addToList(node);
            return this.hashMap.get(key).val;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (this.hashMap.containsKey(key)) {
            Node nodeToRemove = this.hashMap.get(key);
            deleteNode(nodeToRemove);
            Node nodeToAdd = new Node(key, value, null, null);
            addToList(nodeToAdd);
            this.hashMap.put(key, nodeToAdd);
        } else {
            if (this.hashMap.size() == this.capacity) {
                Node nodeToRemove = this.tail.prev;
                int keyToRemove = nodeToRemove.key;
                this.hashMap.remove(keyToRemove);
                deleteNode(nodeToRemove);
            }
            Node nodeToAdd = new Node(key, value, null, null);
                this.hashMap.put(key, nodeToAdd);
                addToList(nodeToAdd);
        }
    }

    class Node {
        int key;
        int val;
        Node prev;
        Node next;

        public Node(int key, int val, Node prev, Node next) {
            this.key = key;
            this.val = val;
            this.prev = prev;
            this.next = next;
        }
    }
    private void addToList(Node nodeToAdd) {
        Node next = this.head.next;
        nodeToAdd.next = next;
        next.prev = nodeToAdd;
        this.head.next = nodeToAdd;
        nodeToAdd.prev = this.head;
    }

    private void deleteNode(Node nodeToRemove) {
        Node next = nodeToRemove.next;
        Node prev = nodeToRemove.prev;
        next.prev = prev;
        prev.next = next;
    }
}
