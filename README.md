# 基於 UDP 協議的多人聊天室

## 傳遞訊息格式：`指令碼::訊息`

```
# 設定新使用者
__newUser__::使用者名稱

# 傳遞訊息
__message__::[使用者名稱]: 訊息

# 離開伺服器
__exit__::__exit__
```

## 使用步驟

1. 輸入伺服器端 IP

2. 輸入英文名稱

3. 輸入訊息，按下 Enter 離開

4. 輸入 `__exit__` 離開聊天室

## Bug

使用非正常方式離開聊天室會導致伺服器端錯誤。


