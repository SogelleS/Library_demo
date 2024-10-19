# coding:utf-8
from decimal import Decimal


class Design:
    """这是Design类，被用来存放读取到的design数据

    Design类的一个Design对象储存了11个变量

    Attributes:
        name: 字符串格式的Design名字
        lower_left_x: 左下角点的x坐标 mm
        lower_left_y: 左下角点的y坐标 mm
        upper_right_x: 右上角点的x坐标 mm
        upper_right_y: 右上角点的y坐标 mm
        polygon_count: 多边形数量
        md5sum: md5sum
        area_length: 区域长度 mm
        area_width: 区域宽度 mm
        area: 区域面积 mm^2
        density: 多边形密度 polygons per mm^2

    """

    def __init__(self, name: str, lower_left_x: str, lower_left_y: str,
                 upper_right_x: str, upper_right_y: str, polygon_count: str,
                 md5sum: str) -> None:
        """Initialise instances based on incoming parameters

        args:
            name: 字符串格式的Design名字
            lower_left_x: 左下角点的x坐标
            lower_left_y: 左下角点的y坐标
            upper_right_x: 右上角点的x坐标
            upper_right_y: 右上角点的y坐标
            polygon_count: 多边形数量
            md5sum: md5sum
        """

        self.name = name
        self.lower_left_x = Decimal(lower_left_x) / Decimal("1000")     # 微米转换为毫米
        self.lower_left_y = Decimal(lower_left_y) / Decimal("1000")
        self.upper_right_x = Decimal(upper_right_x) / Decimal("1000")
        self.upper_right_y = Decimal(upper_right_y) / Decimal("1000")
        self.polygon_count = Decimal(polygon_count)
        self.md5sum = md5sum

        self.area_length = Decimal(upper_right_x) - Decimal(lower_left_x)   # 计算长度
        self.area_width = Decimal(upper_right_y) - Decimal(lower_left_y)    # 计算宽度
        self.area = Decimal(self.area_width) * Decimal(self.area_length)    # 计算面积
        self.density = Decimal(self.polygon_count) / Decimal(self.area)     # 计算密度


        self.area_width = Decimal(upper_right_x) - Decimal(lower_left_x)
        self.area_length = Decimal(upper_right_y) - Decimal(lower_left_y)
        self.area = Decimal(self.area_width) * Decimal(self.area_length)
        self.density = Decimal(self.polygon_count) / Decimal(self.area)


class Library:
    """这是Library类，被用来存储所有的Design的实例并进行排序。

    这是Library的类用来存储Design实例和实现按密度排序

    Attributes:
        design_list: 用来存储Design实例的列表
    """
    def __init__(self) -> None:
        """初始化Library对象,创建空的存储列表"""
        self.design_list = []

    def add_design(self, design_object: Design) -> None:
        """将Design的实例添加到列表design_list中

        args:
            design_object: 需要添加的Design实例
        """
        self.design_list.append(design_object)

    def print_reverse_by_density(self) -> None:
        """按密度倒序打印Design实例的名字属性"""
        reversed_list = sorted(self.design_list, key=lambda design_lambda: design_lambda.density, reverse=True)
        # 用密度倒序排序
        for design in reversed_list:
            print(design.name)

    @classmethod
    def print_reverse_by_density_class_method(cls, library_object) -> None:
        """按密度倒序打印Design实例的名字属性"""
        reversed_list = sorted(library_object.design_list, key=lambda design_lambda: design_lambda.density, reverse=True)
        for design in reversed_list:
            print(design.name)


class ReadDataIter:
    """创建一个可以迭代的文本读取迭代器

    为了避免一次性读入过大的testdata.txt文件导致的内存占用过大,创建了一个可迭代类

    Attributes:
        file_pointer: 打开的文件指针
    """
    def __init__(self, path: str) -> None:
        """初始化对象

        path: testdata.txt文件位置
        """
        self.file_pointer = open(path, "r")

    def __iter__(self) -> iter:
        """可迭代对象的iter方法"""
        return self

    def __next__(self) -> str:
        """可迭代对象的next方法

        returns: 返回testdata.txt中的一行字符串数据

        raise:结束迭代器
        """
        line = self.file_pointer.readline()

        if line == "":
            self.file_pointer.close()
            raise StopIteration()
            # 弹出迭代器
        else:
            return line


def store_design_objects(library_objects: Library, path: str = "./testdata.txt") -> None:
    """读取testdata.txt中的数据并存储到Library的一个实例中

    args:
        library_objects: 作为存储容器的Library实例
        path: testdata.txt路径, 默认为当前目录下的testdata.txt
    """
    for design in ReadDataIter(path):
        if design == "name	lower left x (um)	lower left y (um)	" \
                     "upper right x (um)	upper right y (um)	polygon " \
                     "count	md5sum\n":
            continue
        else:
            list_of_design = design.split()
            # 字符串拆分,用空格或者制表符拆分

            library_objects.add_design(Design(*list_of_design))
            # Design对象添加到Library实例中
            # print(list_of_design)


if __name__ == '__main__':
    library = Library()             # 创建library对象
    store_design_objects(library)   # 读取和存储Design对象
    library.print_reverse_by_density()  # 打印按密度倒序排序的名字

