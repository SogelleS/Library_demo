# coding:utf-8
from decimal import Decimal


class Design:
    """这是Design类，被用来存放读取到的design数据

    """
    def __init__(self, name: str, lower_left_x: str, lower_left_y: str,
                 upper_right_x: str, upper_right_y: str, polygon_count: str,
                 md5sum: str) -> None:

        self.name = name
        self.lower_left_x = Decimal(lower_left_x) / Decimal("1000")
        self.lower_left_y = Decimal(lower_left_y) / Decimal("1000")
        self.upper_right_x = Decimal(upper_right_x) / Decimal("1000")
        self.upper_right_y = Decimal(upper_right_y) / Decimal("1000")
        self.polygon_count = Decimal(polygon_count)
        self.md5sum = md5sum
        self.area_length = Decimal(upper_right_x) - Decimal(lower_left_x)
        self.area_width = Decimal(upper_right_y) - Decimal(lower_left_y)
        self.area = Decimal(self.area_width) * Decimal(self.area_length)
        self.density = Decimal(self.polygon_count) / Decimal(self.area)
        # print(self.area_width)
        # print(self.area_length)
        # print(self.area)


class Library:
    """这是Library类，被用来存储所有的Design的实例并进行按实例的属性进行排序等操作。

    """
    def __init__(self) -> None:
        """

        """
        self.design_list = []

    def add_design(self, design_object: Design) -> None:
        """


        """
        self.design_list.append(design_object)

    def print_reverse_by_density(self) -> None:
        """


        """
        reversed_list = sorted(self.design_list, key=lambda design_lambda: design_lambda.density, reverse=True)
        for design in reversed_list:
            print(design.name)


class ReadDataIter:
    """

    """
    def __init__(self, path: str) -> None:
        self.file_pointer = open(path, "r")

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> str:
        line = self.file_pointer.readline()

        if line == "":
            self.file_pointer.close()
            raise StopIteration()
        else:
            return line


def store_design_objects(library_objects: Library, path: str ="./testdata.txt") -> None:
    """

    :return:
    """
    for design in ReadDataIter(path):
        if design == "name	lower left x (um)	lower left y (um)	" \
                     "upper right x (um)	upper right y (um)	polygon " \
                     "count	md5sum\n":
            continue
        else:
            list_of_design = design.split()
            # library_objects.add_design(Design(list_of_design[0], list_of_design[1], list_of_design[2],
            #                            list_of_design[3], list_of_design[4], list_of_design[5],
            #                            list_of_design[6]))
            library_objects.add_design(Design(*list_of_design))
            # print(list_of_design)


if __name__ == '__main__':
    library = Library()
    store_design_objects(library)
    library.print_reverse_by_density()

