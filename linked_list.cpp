#include <iostream>
#include <sstream>

using namespace std;

int main() {

}

template <typename T>
class DoublyLinkedList 
{
	public: 
	class Node {
		private:
			T data = nullptr; 
			Node* next = nullptr;
			Node* prev = nullptr;

		public:
			Node(T data, Node* next, Node* prev)  {
				this->data = data;
				this->next = next;
				this->prev = prev;
			}

			string toString() {
				osstringstream oss;
				oss << data;
				return oss.str();
			}
	};
	private:
		int size = 0;
		Node* head = nullptr;
		Node* tail = nullptr;
	
};

