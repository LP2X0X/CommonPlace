class DoublyLinkedList 
{
	#size = 0;
	#head = null;
	#tail = null;

}

class Node 
{
	#data = null;
	#next = null;
	#prev = null; 

	constructor (data, next, prev) 
	{
		this.data = data;
		this.next = next;
		this.prev = prev;
	}

	toString() 
	{
		return data.toString();
	}

}
