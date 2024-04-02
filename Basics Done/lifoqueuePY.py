
import queue

book_stack = queue.LifoQueue(maxsize=0)
book_stack.put("The misunderstanding")
book_stack.put("Persepolis")
book_stack.put("1984")

print("The Size is ",book_stack.qsize())
print(book_stack.get())
print(book_stack.get())
print(book_stack.get())