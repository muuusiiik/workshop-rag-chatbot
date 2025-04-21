### WORKSHOP RAG CHATBOT
run the service
```sh
uvicorn app.main:app --reload --port 8000
```

bind to ngrok
```sh
ngrok http http://localhost:8000
```

NOTE: in case of mac silicon user, please following the method 
```sh
https://dashboard.ngrok.com/get-started/setup/macos
```
