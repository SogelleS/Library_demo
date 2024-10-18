import re
import sys

class Design:
    """这是Design类，被用来存放读取到的design数据

    """
    pass


class Library:
    """这是Library类，被用来存储所有的Design的实例并进行按实例的属性进行排序等操作。

    """
    def __init__(self):
        """

        """
        self.design_list = []

    def add_design(self, design_object: Design):
        """

        :return:
        """
        self.design_list.pop(design_object)

    def print_reverse_by_density():
        """

        :return:
        """
        pass


class ReadDataIter:
    """

    """
    def __init__(self):
        self.file_pointer = open("./testdata.txt", "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file_pointer.readline()

        if line == "":
            self.file_pointer.close()
            raise StopIteration()
        else:
            return line


def read_data_from_file():
    """读取数据的函数，数据应位于./testdata.txt文件内，返回一个字符串对象

    :return:
    """
    # with open("./testdata.txt", "r") as file_pointer:
    #     line = " "
    #     while line != "":
    #         line = file_pointer.readline()
    #         print(line, end="")



if __name__ == '__main__':
    for i in ReadDataIter():
        print(i)

