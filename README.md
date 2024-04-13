<p align="left">
    <span>
        <b>中文</b>
    </span>
    <span> • </span>
    <a href="README_en.md">
        English
    </a>
</p>

## 介绍

* `Final_plan.py`这是一个使用Tkinter编写的辞职信界面，你无法拒绝和关闭的辞职信，  
  我认为它十分有趣，内部有十分详细的注释，遇到任何问题，请提 [Issue](https://github.com/hiroi-sora/Umi-OCR/issues) ，我会尽可能帮助你。

## 使用方法

* 直接运行即可

## 自定义图片

1. 如果你想要自定义图片可以直接在`photo`文件夹中修改，把原图片删除，  
   把你需要使用的图片放到`photo`文件夹下  
   需要替换的原图片名称不要变，如：`img_1.png`, `img_2.png`

2. 如果要减少或增加显示的图片可以在代码的第139行，  
   把数字也进行相应的修改
    ```python
    frames = [tk.Frame(root) for _ in range(8)]
    ```
   数字8即表示一直显示到第八张图片`img_8.png`，  
   要显示几张图片就把数字8修改成几，如果是添加，需要在`photo`文件夹下  
   以`img_数字.png`的名称添加图片

## 恶搞

> Final_plan_spoof.py可能会被识别病毒或恶意程序，需要你以管理员权限运行，  
> 运行后如果你巧合的点击到了`反对`按钮，那么你的电脑将会被关机

## 预览截图

![2024-04-13_15-09-29.png](https://s2.loli.net/2024/04/13/KIpZTdhrkbQGgjf.png)
![2024-04-13_15-10-06.png](https://s2.loli.net/2024/04/13/B5CzJNIp2OZrn8D.png)
