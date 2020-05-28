# 操作图像
# 来看看最常见的图像缩放操作，只需三四行代码：
import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw


def opreateImg():
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open('D:\mypy1\IO\husky.jpg')
    # 获得图像尺寸:
    w, h = im.size
    # 缩放到50%:
    im.thumbnail((w // 2, h // 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    # 把缩放后的图像用jpeg格式保存:
    im.save(r'D:\mypy1\IO\thumbnail.jpg', 'jpeg')


# opreateImg()

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
#
# 比如，模糊效果也只需几行代码：

def dim_img():
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open('D:\mypy1\IO\husky.jpg')
    # 应用模糊滤镜:
    im = im.filter(ImageFilter.BLUR)
    im.save(r'D:\mypy1\IO\blur.jpg', 'jpeg')


# dim_img()

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def creat_codeimg():
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype(r'D:\mypy1\IO\msjh_boot.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save(r'D:\mypy1\IO\code.jpg', 'jpeg')


# creat_codeimg()

# 要详细了解PIL的强大功能，请请参考Pillow官方文档：
#
# https://pillow.readthedocs.org/
#
# 小结
# PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。
