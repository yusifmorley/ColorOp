import math
import colorsys

#  HColor 类构造 接受r g b 三个参数 转换为H S V
class HColor:
    def __init__(self, r, g, b):
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        self.h = h * 360  # 0-360
        self.s = s  # 0-1
        self.v = v  # 0-1
    # 设置 h的值
    """
    :param hv: int 是角度值
    """
    def pluseH(self, hv:int):
        if self.h + hv > 360:
            return self.h + hv - 360
        return self.h + hv

    # 得到颜色的差值
    def get_difference(self, h, s, v):
        return math.sqrt((self.h - h) ** 2 + (self.s - s) ** 2 + (self.v - v) ** 2)

    # 得到对比度
    def get_contrasting(self):
        return self.pluseH(180), self.s, self.v

    def tor_gb(self):
        return colorsys.hsv_to_rgb(self.h / 360, self.s, self.v)
