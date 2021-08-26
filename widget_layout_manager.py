from tkinter import *


def pack_demo():
    """
    实现主要逻辑
    :return:
    """
    """
    tkinter中一共有三种widget_layout_manager
    pack()
    grid()
    place()
    """
    """
    pack()函数参数解释:
        side:选择部件的布局方式
            TOP 默认,表示放置在顶部,如果多个部件同时都是TOP放置,那么先pack的在上面后放置的在先放置的下面
            BOTTOM 放置在底部
            LEFT 放置在左边
            RIGHT 放置在右边
        padx:和其他组件的水平间距
        pady:和其他组件的垂直间距
        ipadx:控制标签文字与标签容器的x轴间距
        ipady:控制标签文字与标签容器的y轴间距
        anchor:设定Widget控件在窗口中的位置  可以与side参数搭配使用,达到调整布局的效果
        fill:布局的部件在窗口中的填充方式
            X表示填充满整个x轴
            Y表示填充满整个y轴
            BOTH表示填充满整个x轴和y轴
        expand:是否填充满额外的父容器空间
    """
    root_win = Tk()

    # 给窗口添加label
    label1 = Label(root_win, text="python", bg="cyan", width=15)
    label1.pack(side=LEFT, fill=Y)

    label2 = Label(root_win, text="java", bg="lightyellow", width=15)
    label2.pack(fill=X)

    label3 = Label(root_win, text="C++", bg="lightgreen", width=15)
    label3.pack(fill=BOTH, expand=True)

    root_win.mainloop()


def grid_demo():
    """
    grid网格布局
    :return:
    """
    """
    grid(options,...)
    row:组件放在第几行
    column:组件放在第几列
    padx:和其他组件的水平间距
    pady:和其他组件的垂直间距
    rowspan:组件占几行位置
    columnspan:组件占几列位置
    sticky:这个参数的功能类似anchor，但是只可以设定N/S/W/E
    rowconfigure(0, weight=1)和columnconfigure(0, weight=1),这两个方法是主窗口的方法,需要使用主窗口调用
    rowconfigure:表示row 0的组件当窗口改变大小的时候缩放比例是1
    columnconfigure:表示column 0的组件当窗口改变大小的时候缩放比例是1
    """
    root = Tk()
    # rowconfigure(0, weight=1)和columnconfigure(0, weight=1)
    # rowconfigure:表示row 0的组件当窗口改变大小的时候缩放比例是1
    # columnconfigure:表示column 0的组件当窗口改变大小的时候缩放比例是1
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)


    label1 = Label(root, text="python", bg="cyan", width=15)
    label2 = Label(root, text="java", bg="yellow", width=15)
    label3 = Label(root, text="C++", bg="green", width=15)

    label1.grid(row=0, column=0, columnspan=2, stick=N+S+W+E) # 网格布局,设置在第0行 第0列 占用2列位置, 并且左右拉伸,填充不足的部分
    label2.grid(row=1, column=0)
    label3.grid(row=1, column=1)

    root.mainloop()


def place_demo():
    """
    place布局
    直接指定方式将Widget控件放在容器（可想成窗口）中的方法
    :return:
    """
    """
    place(options,......)
        height/width:设置组件的实际大小
        relx/rely:设置相对于父容器（可想成父窗口）的位置
        x/y:指定放置的组件的左上角在主窗口中的位置,单位是像素
        relheight/relwidth:设置相对于父容器（可想成父窗口）的大小
        bordermode
        anchor
    """
    root = Tk()
    root.title("place")

    rain_image = PhotoImage(file='R-C.gif')
    # label1 = Label(root, text='python', bg='cyan', width=15)
    # label2 = Label(root, text='java', bg='yellow', width=15)
    # label3 = Label(root, text='C++', bg='green', width=15)
    #
    # label1.place(x=0, y=0)
    # label2.place(x=30, y=30)
    # label3.place(x=60, y=60, width=400, height=240)

    label4 = Label(root, image=rain_image)
    label4.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) # 设置相对距离为0.1, 相对大小为0.8

    root.mainloop()


if __name__ == '__main__':
    place_demo()
