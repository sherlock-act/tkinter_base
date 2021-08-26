from tkinter import *
import time


def simple_button_demo():
    """
    按钮调试
    :return:
    """
    """
    button(父对象, options)
    1）borderwidth或bd：边界宽度默认是两个像素。
    （2）bg或background：背景色彩。
    （3）command：单击功能按钮时，执行此方法。
    （4）cursor：当鼠标光标移至按钮上时的形状。
    （5）fg或foreground：前景色彩。
    （6）font：字形。
    （7）height：高，单位是字符高。
    （8）highlightbackground：当功能按钮取得焦点时的背景颜色。
    （9）highlightcolor：当功能按钮取得焦点时的颜色。
    （10）image：功能钮上的图像。
    （11）justify：当有多行文字时，最后一行文字的对齐方式。
    （12）padx：默认是1，可设置功能按钮与文字的间隔。
    （13）pady：默认是1，可设置功能按钮的上下间距。
    （14）relief：默认是relief=FLAT，可由此控制文字外框。
    （15）state：默认是state=NORMAL，若设置为DISABLED则以灰阶显示功能按钮，表示暂时无法使用。
    （16）text：功能按钮名称。
    （17）underline：可以设置第几个文字有下画线，从0开始算起，默认是-1表示无下画线。
    （18）width：宽，单位是字符宽。
    （19）wraplength：限制每行的文字数，默认是0，表示只有“\n”才会换行。
    """

    def show_label():
        label.config(text="python", bg="cyan")

    root = Tk()

    # 点击按钮,显示标签信息
    label = Label(root)
    btn1 = Button(root, text="点击显示", command=show_label)
    # quit与destroy都可以实现关系当前窗口,停止程序的效果
    btn2 = Button(root, text='关闭', command=root.destroy)

    label.pack()
    btn1.pack(side=LEFT)
    btn2.pack(side=RIGHT)

    root.mainloop()


def datetime_button_demo():
    """
    实现时间显示,与退出
    并且可以更换背景色的功能
    :return:
    """
    """
    button(父对象, options)
    1）borderwidth或bd：边界宽度默认是两个像素。
    （2）bg或background：背景色彩。
    （3）command：单击功能按钮时，执行此方法。
    （4）cursor：当鼠标光标移至按钮上时的形状。
    （5）fg或foreground：前景色彩。
    （6）font：字形。
    （7）height：高，单位是字符高。
    （8）highlightbackground：当功能按钮取得焦点时的背景颜色。
    （9）highlightcolor：当功能按钮取得焦点时的颜色。
    （10）image：功能钮上的图像。
    （11）justify：当有多行文字时，最后一行文字的对齐方式。
    （12）padx：默认是1，可设置功能按钮与文字的间隔。
    （13）pady：默认是1，可设置功能按钮的上下间距。
    （14）relief：默认是relief=FLAT，可由此控制文字外框。
    （15）state：默认是state=NORMAL，若设置为DISABLED则以灰阶显示功能按钮，表示暂时无法使用。
    （16）text：功能按钮名称。
    （17）underline：可以设置第几个文字有下画线，从0开始算起，默认是-1表示无下画线。
    （18）width：宽，单位是字符宽。
    （19）wraplength：限制每行的文字数，默认是0，表示只有“\n”才会换行。
    """

    def bcolor(color):
        label.config(bg=color)

    def time_run(l_widget):
        def show_now():
            l_widget.config(text=time.strftime("%Y-%m-%d %X", time.localtime()))
            l_widget.after(1000, show_now)

        show_now()

    root = Tk()

    label = Label(root, bg="yellow", fg='blue', height=3, width=20)
    btn1 = Button(root, text="退出", command=root.destroy, cursor="hand2")
    btn2 = Button(root, text="yellow", command=lambda: bcolor("yellow"), cursor="hand2")
    btn3 = Button(root, text="cyan", command=lambda: bcolor("cyan"), cursor="hand2")

    label.grid(row=0, column=0, columnspan=3)
    time_run(label)
    btn2.grid(row=1, column=0)
    btn3.grid(row=1, column=1)
    btn1.grid(row=1, column=2)

    root.mainloop()


if __name__ == '__main__':
    datetime_button_demo()
