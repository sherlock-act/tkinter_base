import tkinter as tk


def main():
    root = tk.Tk() # 主窗口
    # 调整计算器的大小
    root.title("计算器")
    # root.geometry("616x665")

    # 添加组件
    title_label = tk.Label(root, width=90, height=2, bg="lightyellow")
    result_label = tk.Label(root, width=90, height=2, bg="lightyellow")

    title_label.grid(row=0, column=0, columnspan=4)
    result_label.grid(row=1, column=0, columnspan=4)
    tk.Button(root, text="7", width=20, height=2).grid(row=2, column=0)
    tk.Button(root, text="8", width=20, height=2).grid(row=2, column=1)
    tk.Button(root, text="9", width=20, height=2).grid(row=2, column=2)
    tk.Button(root, text="/", width=20, height=2).grid(row=2, column=3)
    tk.Button(root, text="4", width=20, height=2).grid(row=3, column=0)
    tk.Button(root, text="5", width=20, height=2).grid(row=3, column=1)
    tk.Button(root, text="6", width=20, height=2).grid(row=3, column=2)
    tk.Button(root, text="*", width=20, height=2).grid(row=3, column=3)
    tk.Button(root, text="1", width=20, height=2).grid(row=4, column=0)
    tk.Button(root, text="2", width=20, height=2).grid(row=4, column=1)
    tk.Button(root, text="3", width=20, height=2).grid(row=4, column=2)
    tk.Button(root, text="+", width=20, height=2).grid(row=4, column=3)
    tk.Button(root, text="0", width=20, height=2).grid(row=5, column=0)
    tk.Button(root, text=".", width=20, height=2).grid(row=5, column=1)
    tk.Button(root, text="=", width=20, height=2).grid(row=5, column=2)
    tk.Button(root, text="-", width=20, height=2).grid(row=5, column=3)

    root.mainloop() # 主窗口循环显示


if __name__ == '__main__':
    main()
