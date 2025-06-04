import tkinter as tk

# 設定處理按鈕點擊事件的函數
def show_input():
    user_input = entry.get()  # 取得使用者輸入的文字
    label.config(text=f"你輸入的是: {user_input}")  # 顯示輸入的文字

# 創建主視窗
root = tk.Tk()
root.title("文字輸入範例")
root.geometry("300x200")

# 創建標籤 (Label)
label = tk.Label(root, text="請輸入一些文字：")
label.pack(pady=10)

# 創建文字輸入框 (Entry)
entry = tk.Entry(root)
entry.pack(pady=10)

# 創建按鈕 (Button)
button = tk.Button(root, text="顯示輸入的文字", command=show_input)
button.pack(pady=10)

# 開始主事件循環
root.mainloop()
