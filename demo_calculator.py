import tkinter as tk


def calculator():
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))

def show(buttonstring):
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonstring)

def backspace():
    """
    删除前一个字符
    :return:
    """
    equ.set(equ.get()[:-1])


def clear():
    """
    清除显示区,设置为0
    :return:
    """
    equ.set("0")




root = tk.Tk() # 主窗口
# 调整计算器的大小
root.title("计算器")
# root.geometry("616x665")

# 设置默认显示为0
equ = tk.StringVar()
equ.set("0")


# 添加组件
title_label = tk.Label(root, width=24, height=2, bg="lightyellow", relief="raised", textvariable=equ, anchor="se")

title_label.grid(row=0, column=0, columnspan=4)
# 清除按钮
clear_button = tk.Button(root, text="C", width=5, command=clear)
clear_button.grid(row=1, column=0)

# row1的其他按钮
tk.Button(root, text="DEL", width=5, command=backspace).grid(row=1, column=1)
tk.Button(root, text="%", width=5, command=lambda: show("%")).grid(row=1, column=2)
tk.Button(root, text="/", width=5, command=lambda: show("/")).grid(row=1, column=3)

# row2的按钮
tk.Button(root, text="7", width=5, command=lambda: show("7")).grid(row=2, column=0)
tk.Button(root, text="8", width=5, command=lambda: show("8")).grid(row=2, column=1)
tk.Button(root, text="9", width=5, command=lambda: show("9")).grid(row=2, column=2)
tk.Button(root, text="*", width=5, command=lambda: show("*")).grid(row=2, column=3)

# row3的按钮
tk.Button(root, text="4", width=5, command=lambda: show("4")).grid(row=3, column=0)
tk.Button(root, text="5", width=5, command=lambda: show("5")).grid(row=3, column=1)
tk.Button(root, text="6", width=5, command=lambda: show("6")).grid(row=3, column=2)
tk.Button(root, text="-", width=5, command=lambda: show("-")).grid(row=3, column=3)

# row4的按钮
tk.Button(root, text="1", width=5, command=lambda: show("1")).grid(row=4, column=0)
tk.Button(root, text="2", width=5, command=lambda: show("2")).grid(row=4, column=1)
tk.Button(root, text="3", width=5, command=lambda: show("3")).grid(row=4, column=2)
tk.Button(root, text="+", width=5, command=lambda: show("+")).grid(row=4, column=3)

# row5的按钮
tk.Button(root, text="0", width=12, command=lambda: show("0")).grid(row=5, column=0, columnspan=2)
tk.Button(root, text=".", width=5, command=lambda: show(".")).grid(row=5, column=2)
tk.Button(root, text="=", width=5, bg="yellow",  command=lambda: calculator()).grid(row=5, column=3)


root.mainloop() # 主窗口循环显示


