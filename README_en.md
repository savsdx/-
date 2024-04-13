<p align="left">
    <a href="README.md">
        中文
    </a>
    <span> • </span>
    <span>
        <b>English</b>
    </span>
    

</p>

## Introduction

* `Final_plan.py` is a resignation letter interface written using Tkinter that you cannot refuse or close. I find it
  quite interesting, with detailed comments inside. If you encounter any issues, please raise
  an [Issue](https://github.com/hiroi-sora/Umi-OCR/issues), and I will try to help you as much as possible.

## Usage

* Simply run it.

## Customizing Images

1. If you want to customize the images, you can directly modify them in the `photo` folder. Delete the original images
   and place the images you want to use in the `photo` folder. Do not change the names of the original images to be
   replaced, such as `img_1.png`, `img_2.png`.

2. If you want to reduce or increase the number of displayed images, you can modify the number on line 139 of the code
   accordingly:
    ```python
    frames = [tk.Frame(root) for _ in range(8)]
    ```
   The number 8 indicates that it will display images up to the eighth image `img_8.png`. To display a different number
   of images, modify the number to the desired value. If you are adding images, they need to be added in the `photo`
   folder with names like `img_数字.png`.

## Prank

> `Final_plan_spoof.py` may be recognized as a virus or malicious program. You need to run it with administrator
> privileges. If you accidentally click the "Oppose" button, your computer will shut down.

## Preview Screenshots

![2024-04-13_15-09-29.png](https://s2.loli.net/2024/04/13/KIpZTdhrkbQGgjf.png)
![2024-04-13_15-10-06.png](https://s2.loli.net/2024/04/13/B5CzJNIp2OZrn8D.png)
