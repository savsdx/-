import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from random import random
# import os

"""
删除了多余的注释和print，没有创建组件类，没有索要管理员权限
"""


def center_window(window, width, height):
    # 获取屏幕宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口的位置
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # 设置窗口位置
    window.geometry(f'{width}x{height}+{x}+{y}')


def resize_image(image_path, width, height):
    # 打开图片并按比例缩小
    original_image = Image.open(image_path)
    original_width, original_height = original_image.size
    # 计算图片的宽高比
    aspect_ratio = original_width / original_height
    # 如果 target_width / aspect_ratio <= target_height，意味着以目标宽度作为标准,按原始宽高比计算的高度,不会超过目标高度，
    # 不会超过就可以直接修改,以目标宽度为基准进行缩放。
    if width / aspect_ratio <= height:
        resized_height = int(width / aspect_ratio)
        resized_width = width
    # 如果 target_width / aspect_ratio > target_height，意味着以目标宽度作为标准,按原始宽高比计算图片的高度,会超过目标高度，
    # 按照宽度为标准,高度会超出一截,无法显示出来,所以就以目标高度作为标准,按原始宽高比计算图片的宽度
    else:
        resized_width = int(height * aspect_ratio)
        resized_height = height
    resized_image = original_image.resize((resized_width, resized_height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


def on_exit():
    tk.messagebox.showinfo(title='提示', message='此路不通')


# 创建主窗口
root = tk.Tk()
root.title("辞职信——")

# 设置主窗口大小
window_width = 700
window_height = 500

# 设置居中主窗口
center_window(root, window_width, window_height)

# 建立一个框架
frame1 = tk.Frame(root, bd=1, relief='solid')
frame1.pack(expand=True, fill='both')

# 创建一个标签
tk.Label(frame1, text='尊敬的各位领导：', font=24, padx=30, pady=30).pack(side=tk.LEFT, anchor=tk.N)

# 再创建一个标签,放在frame1框架中,标签中放置一张图片
img = tk.PhotoImage(file='photo/img.png')
label_img = tk.Label(frame1, image=img, padx=30, pady=30, bd=0, anchor='n')
label_img.pack(side=tk.LEFT, expand=True, fill='both')

# 设置一个标签,放入文本
tk.Label(frame1, text='辞职人：正心', height=25, font=24, padx=30, pady=30, anchor='se').pack(
    side=tk.LEFT, expand=True, fill='both')

# 设置图片期望的高度和宽度
height_img = 100
width_img = 100

yes_img = resize_image(image_path='photo/img_yes.png', width=width_img, height=height_img)
no_img = resize_image(image_path='photo/img_no.png', width=width_img, height=height_img)

yes_btn = tk.Button(frame1, image=yes_img, bd=4, relief='flat')
no_btn = tk.Button(frame1, image=no_img, bd=0)

yes_btn.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
no_btn.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

# 当用户点击关闭窗口时，执行on_exit函数
root.protocol("WM_DELETE_WINDOW", on_exit)


# 执行关机命令
# no_btn.config(command=lambda: os.system('shutdown /s /t 0'))


def move(event):
    no_btn.place(relx=random(), rely=random(), anchor=tk.CENTER)


# 给按钮绑定一个事件
no_btn.bind('<Enter>', move)

# 初始化一个空的图像对象列表
reason_img_s = []


def improve_sure(frame, index):
    # 调整图片大小
    reason_img = resize_image(image_path=f'./photo/img_{index}.png', width=400, height=350)
    reason_img_s.append(reason_img)

    tk.Label(frame, text='离职原因：', font=24, padx=30, pady=30, anchor='w').pack(side='top', anchor='w')

    tk.Label(frame, image=reason_img, font=24, padx=30, pady=30, anchor='n').pack(side='top', anchor='center',
                                                                                  expand=True,
                                                                                  fill='y')
    next_button = tk.Button(frame, text='再也不见', command=root.quit)
    next_button.place(relx=0.85, rely=0.9, anchor='center')
    return next_button


def create_switch_function(current_frame, next_frame, current_btn, index):
    # 在主窗口内隐藏第一个框架（中的所有组件），把第二个框架布局到窗口中
    def sure():
        current_frame.pack_forget()
        next_frame.pack(expand=True, fill='both')

    # 在第二个框架框架中布局组件
    but2 = improve_sure(next_frame, index)

    # 重新配置第一个框架中按钮的参数
    current_btn.config(command=sure)

    return but2


# 创建帧对象
frames = [tk.Frame(root) for _ in range(8)]

# 通过循环创建帧之间的切换关系
buttons = []
for i in range(len(frames)):  # i的取值范围从0到7
    if i == 0:
        buttons.append(yes_btn)
        button = create_switch_function(frame1, frames[i], buttons[-1], i + 1)
    else:
        button = create_switch_function(frames[i - 1], frames[i], buttons[-1], i + 1)

    buttons.append(button)

# 运行主循环
root.mainloop()
