from fastapi import FastAPI, HTTPException

app = FastAPI()

# Handling text posts

text_posts = {
    1: {"title": "New Post", "content": "This is a test post"},
    2: {"title": "FastAPI Intro", "content": "Learning how to build APIs with Python."},
    3: {"title": "Python Tips", "content": "Use type hints for better code clarity."},
    4: {"title": "Web Development", "content": "The frontend and backend must communicate via JSON."},
    5: {"title": "Database Basics", "content": "SQL vs NoSQL: which one should you choose?"},
    6: {"title": "Async Programming", "content": "Understanding await and async in FastAPI."},
    7: {"title": "Deployment", "content": "How to deploy your app using Docker and Uvicorn."},
    8: {"title": "Middleware", "content": "Adding custom headers to every response."},
    9: {"title": "Security", "content": "Always hash your passwords before storing them."},
    10: {"title": "Testing", "content": "Writing unit tests with Pytest for your endpoints."}
}


@app.get("/posts")
def get_all_post(limit: int = None): # Limit is an optional query parameter. Query parameters are the ones that appear after the '?'
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not fo")

    return text_posts.get(id)


