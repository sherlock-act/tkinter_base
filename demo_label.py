from tkinter import *
import time
from tkinter import ttk


def set_root_window(root_win):
    """
    设置主窗口参数
    :param root_win: 主窗口对象
    :return:  root_win
    """
    # 给窗口设置标题名称
    root_win.title("测试窗口")
    # 设置窗口的大小与位置 宽x高+左上角x坐标+左上角y坐标
    # root_win.geometry("500x500+100+100")
    # 设置窗口最大像素
    # root_win.maxsize(1200, 900)
    # 设置窗口最小像素
    # root_win.minsize(100, 100)
    # 设置窗口背景颜色
    # root_win.configure(bg="gray")
    # 设置窗口大小是否可更改,两个参数分别代表宽高是否可更改
    # root_win.resizable(False, False)
    # 修改窗口的图标
    root_win.iconbitmap("./wpsbox.ico")
    # 获取当前屏幕宽度
    screen_width = root_win.winfo_screenwidth()
    # 获取当前屏幕高度
    screen_height = root_win.winfo_screenheight()
    # 设置窗口宽高与距离窗口左上角的坐标位置
    win_width = 500
    win_height = 300
    win_x = (screen_width - win_width) / 2
    win_y = (screen_height - win_height) / 2
    # 设置窗口大小并且在屏幕中间显示
    root_win.geometry("{}x{}+{}+{}".format(win_width, win_height, int(win_x), int(win_y)))

    return root_win


def run_count(win_widget):
    """
    实现展示当前时间功能
    :param win_widget:  部件
    :return:
    """
    def number_count():
        """
        实现展示当前时间
        :return:
        """
        now_time = time.strftime("%Y-%m-%d %X", time.localtime())
        win_widget.config(text=str(now_time))
        win_widget.after(1000, number_count)

    number_count()


def set_label(root_win):
    """
    添加标签设置
    :param root_win: 主窗口
    :return: root_win
    """
    """
    text:label中要显示的文本信息
    foreground:前景色 也可以看做是字体颜色
    background:背景色
    width:修改标签的宽度
    height:修改标签的高度
    anchor:锚定,即标签的位置,分别使用东西南北表示,西南就是sw,还有一个中间使用center表示
    wraplength:设置标签中的文字在多少宽度后自动换行
    font:设置文本字体信息
        1）字形family：如Helvetica、Times等，读者可以进入Word内参考所有系统字形。
        2）字号size：单位是像素。
        3）加粗weight：例如bold、normal。
        4）倾斜slant：例如italic、roman，如果不是italic则是roman。
        5）下划线underline
        6）删除线overstrike
    justify:文本最后一行输出内容布局方式, left/center/right
    image:label中显示图像信息
    bitmap:系统内建位图信息
        error, hourglass, info, questhead, question, warning, gray12, gray25, gray50, gray75
    compound:设置文字与图像的位置关系
        left：图像在左。right：图像在右。top：图像在上。bottom：图像在下。center：文字覆盖在图像上方。
    relief:边框样式
        groove, raised, ridge, solid, sunken
    padx:标签中的文本距离左右两边的距离
    pady:标签中的文本距离上下两边的距离
    Cursors:鼠标悬停的时候鼠标的样式
    """
    # 显示图像
    global photo
    # 必须设置为全局变量，否则本方法执行完毕后图片对象销毁，窗口无法显示图像
    photo = PhotoImage(file="R-C.gif")  # 导入图像
    label = Label(root_win,
                  text="i love program\npython",
                  foreground="cyan",
                  # background="red",
                  # width=20,
                  # height=10,
                  anchor="center",
                  # wraplength=40,
                  font="Helvetica 20 bold italic underline overstrike",
                  justify="left",
                  image=photo,
                  # bitmap="error",
                  compound="center",
                  relief="ridge",
                  padx=10,
                  pady=5,
                  cursor="star"
                  )
    label.pack()

    # 使用keys()函数可以获取所有的属性
    # print(label.keys())


def main():
    """
    主要逻辑
    :return:
    """
    """
    config()函数:可以修改部件中的参数
    keys()函数:返回该部件的所有参数
    """
    # 创建tk对象,建立主窗口
    root_win = Tk()

    # 设置主窗口参数
    root_win = set_root_window(root_win)

    # 设置label
    set_label(root_win)

    # 在ttk中的Separator函数可以绘制一根分割线
    sep = ttk.Separator(root_win, orient=HORIZONTAL)
    # 设置分割线长度为整个窗口的宽度,并且距离左右两边5像素
    sep.pack(fill=X, padx=5)

    # 定义一个标签,展示当前系统时间
    label2 = Label(foreground="red",
                   compound="center",
                   font="Helvetica 20 bold italic underline overstrike",
                   cursor="heart")
    label2.pack()
    run_count(label2)

    root_win.mainloop()


if __name__ == '__main__':
    main()
