from django.shortcuts import render

stack = []
queue = []
stack_history = []
queue_history = []

def home(request):
    if request.method == "POST":
        action = request.POST.get("action")
        value = request.POST.get("value", "")

        # Stack operations
        if action == "push" and value:
            stack.append(value)
            stack_history.append(f"✅ Pushed '{value}' to Stack")

        elif action == "pop":
            if stack:
                removed = stack.pop()
                stack_history.append(f"🗑️ Popped '{removed}' from TOP")
            else:
                stack_history.append("❌ Stack is Empty!")

        # Queue operations
        elif action == "enqueue" and value:
            queue.append(value)
            queue_history.append(f"✅ Enqueued '{value}' to Queue")

        elif action == "dequeue":
            if queue:
                removed = queue.pop(0)
                queue_history.append(f"🗑️ Dequeued '{removed}' from FRONT")
            else:
                queue_history.append("❌ Queue is Empty!")

        # Clear operations
        elif action == "clear_stack":
            stack.clear()
            stack_history.clear()

        elif action == "clear_queue":
            queue.clear()
            queue_history.clear()

    return render(request, "index.html", {
        "stack": stack,
        "queue": queue,
        "stack_history": stack_history,
        "queue_history": queue_history,
        "stack_size": len(stack),
        "queue_size": len(queue),
    })