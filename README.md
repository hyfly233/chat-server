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

## Speech-to-Text Functionality

To use the speech-to-text functionality, send a POST request to the following endpoint:

```
POST /transcribe
```

### Request Body

The request body should contain the audio file to be transcribed.

### Response

```json
{
    "text": "Transcribed text"
}
```

## Text-to-Speech Functionality

To use the text-to-speech functionality, send a POST request to the following endpoint:

```
POST /synthesize
```

### Request Body

```json
{
    "text": "Text to be converted to speech"
}
```

### Response

```json
{
    "message": "Text has been converted to speech",
    "file": "output.mp3"
}
```

## Audio File to Data Stream Functionality

To use the audio file to data stream functionality, send a POST request to the following endpoint:

```
POST /audio_stream
```

### Request Body

The request body should contain the audio file to be converted to a data stream.

### Response

```json
{
    "audio_stream": "Base64 encoded audio stream"
}
```
