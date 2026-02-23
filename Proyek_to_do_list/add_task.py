def add_task(tasks, title, created_at, deadline):
    tasks.append({
        "title": title,
        "done": False,
        "created_at": created_at,
        "deadline": deadline
    })