```shell
uv pip install SpeechRecognition -i https://pypi.tuna.tsinghua.edu.cn/simple

uv add SpeechRecognition 
```

http://127.0.0.1:18000/llama3/test/invoke
```json
{
    "input": {
        "text": "what is java"
    }
}
```

## Chat Functionality

To use the chat functionality, send a POST request to the following endpoint:

```
POST /chat/{session_id}
```

### Request Body

```json
{
    "text": "Your message here"
}
```

### Response

```json
{
    "response": "Chatbot's response"
}
```

## Viewing Historical Messages

To view historical messages, send a GET request to the following endpoint:

```
GET /history/{session_id}
```

### Response

```json
{
    "history": [
        {"role": "user", "content": "User's message"},
        {"role": "assistant", "content": "Chatbot's response"}
    ]
}
```
