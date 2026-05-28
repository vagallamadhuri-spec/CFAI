from django.shortcuts import render

stack = []
queue = []
stack_log = []
queue_log = []

def home(request):
    if request.method == "POST":
        action = request.POST.get("action")
        values = request.POST.get("value", "")

        if action == "push" and values:
            numbers = values.split()
            for num in numbers:
                stack.append(num)
                queue.append(num)
                stack_log.append(f"✅ {num} is pushed to Stack")
                queue_log.append(f"✅ {num} is enqueued to Queue")

        elif action == "pop":
            if stack:
                removed = stack.pop()
                stack_log.append(f"🗑️ {removed} is popped from Stack")
            else:
                stack_log.append("❌ Stack is Empty!")

        elif action == "dequeue":
            if queue:
                removed = queue.pop(0)
                queue_log.append(f"🗑️ {removed} is dequeued from Queue")
            else:
                queue_log.append("❌ Queue is Empty!")

        elif action == "clear":
            stack.clear()
            queue.clear()
            stack_log.clear()
            queue_log.clear()

    return render(request, "index.html", {
        "stack": stack,
        "queue": queue,
        "stack_log": stack_log,
        "queue_log": queue_log,
        "stack_size": len(stack),
        "queue_size": len(queue),
    })