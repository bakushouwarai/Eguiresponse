greetings = [
    "こんにちは",
    "こんちゃ",
    "おはよう",
    "こんばんは",
    "hello",
    "hi",
    "hey",
    "やあ",
    "よっ"
]

print("挨拶すると『エグい』って返します。終了するには exit と入力。")

while True:
    text = input("あなた: ").strip().lower()

    if text == "exit":
        print("終了します。")
        break

    if any(greeting in text for greeting in greetings):
        print("ツール: エグい")
    else:
        print("ツール: 挨拶してくれ")
