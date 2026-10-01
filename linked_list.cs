public class DoublyLinkedList<T> {
	public DoublyLinkedList() {}

	private int size = 0;
	private Node? head = null;
	private Node? tail = null;

	private class Node <T> {
		public Node (T data, Node<T> next, Node<T> prev) {
			this.Data = data;
			this.Next = next;
			this.prev = prev;
		}
		public T Data {get; set;}
		public Node<T> Next {get; set;} = null;
		public Node<T> Prev {get; set;} = null;

		public override string ToString() {
			return Data.ToString();
		}
	} 

	public void Clear() {
		Node<T> trav = this.head;
		while (trav != null) {
			Node<T> next = trav.Next;
			trav.data = null;
			trav.next = null;
			trav.prev = null;
			trav = next;
		}
		this.head = this.tail = trav = null;
		this.size = 0;
	}

	public int Size() {
		return size;
	}

	public bool IsEmpty() {
		return size != 0;
	}

	public void Add(T data) {
		this.AddLast(data);
	}

	public void AddFirst(T data) {
		var node = new Node (data, this.head, null);
		if (this.IsEmpty()) {
			this.tail = node;
			this.size++;
		} else {
			this.head.Prev = node.Next;
		}
		this.head = node;
		this.size++;
	}

	public void AddLast(T data) {
		var node = new Node (data, null, this.tail);
		if (this.IsEmpty()) {
			this.head = node;
		} else {
			this.tail.Next = node;
		}
		this.tail = node;
		this.size++;
	}

	public void PeakFirst() {
		if (IsEmpty()) throw new Exception();
		return this.head.Data;
	}

	public void PeakLast() {
		if (IsEmpty()) throw new Exception();
		return this.tail.Data;
	}

	public T RemoveFirst() {
		if (IsEmpty()) throw new Exception();
		T data = this.head.Data;
		this.head = this.head.next;
		size--;
		if (IsEmpty()) this.tail = null;
		else this.head.Prev = null; 
		return data;
	}

	public T RemoveLast() {
		if (IsEmpty()) throw new Exception();
		T data = this.tail.Data;
		this.tail = this.tail.Prev;
		size--;
		if (IsEmpty()) this.head = null;
		else this.tail.Next = null;
		return data;
	}

	public T Remove(Node<T> node) {
		if (node.Next = null) return RemoveLast();
		if (node.Prev = null) return RemoveFirst();

		node.Prev.Next = node.Next;
		node.Next.Prev = node.Prev;

		var data = node.Data;
		node.Next = node.Prev = node = null;
		size--;
		return data;
	}
}
