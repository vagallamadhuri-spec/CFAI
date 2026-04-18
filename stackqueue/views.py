from django.shortcuts import render

stack = []
queue = []

def home(request):
    message = ""

    if request.method == "POST":
        action = request.POST.get("action")
        value = request.POST.get("value", "")

        if action == "push" and value:
            stack.clear()        # ← clears old values
            stack.append(value)
            message = f"Pushed '{value}' to Stack"

        elif action == "pop":
            if stack:
                removed = stack.pop()
                message = f"Popped '{removed}' from Stack"
            else:
                message = "Stack is Empty!"

        elif action == "enqueue" and value:
            queue.clear()        # ← clears old values
            queue.append(value)
            message = f"Enqueued '{value}' to Queue"

        elif action == "dequeue":
            if queue:
                removed = queue.pop(0)
                message = f"Dequeued '{removed}' from Queue"
            else:
                message = "Queue is Empty!"

    return render(request, "index.html", {
        "stack": stack,
        "queue": queue,
        "message": message
    })