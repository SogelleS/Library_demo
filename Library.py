# coding:utf-8
from decimal import Decimal


class Design:
    """This is the Design class, which is used to store the read design data.

    A Design object of the Design class stores 11 variables. Adopt Decimal module for precise calculations.

    Attributes:
        name: the name of the Design in str.
        lower_left_x: x-coordinate of the lower left point (mm).
        lower_left_y: y-coordinate of the lower-left point (mm).
        upper_right_x: x-coordinate of the upper right point (mm).
        upper_right_y: y-coordinate of the upper right point (mm).
        polygon_count: number of polygons.
        md5sum: md5sum.
        area_length: length of the area (mm).
        area_width: width of the area (mm).
        area: area size (mm^2).
        density:  polygon density (polygons per mm^2).
    """

    def __init__(self, name: str, lower_left_x: str, lower_left_y: str,
                 upper_right_x: str, upper_right_y: str, polygon_count: str,
                 md5sum: str) -> None:
        """Initialise instances based on incoming parameters.

        args:
            name: the name of the Design in str.
            lower_left_x: x-coordinate of the lower left point (mm).
            lower_left_y: y-coordinate of the lower-left point (mm).
            upper_right_x: x-coordinate of the upper right point (mm).
            upper_right_y: y-coordinate of the upper right point (mm).
            polygon_count: number of polygons.
            md5sum: md5sum.
        """

        self.name = name
        self.lower_left_x = Decimal(lower_left_x) / Decimal(1000)
        self.lower_left_y = Decimal(lower_left_y) / Decimal(1000)
        self.upper_right_x = Decimal(upper_right_x) / Decimal(1000)
        self.upper_right_y = Decimal(upper_right_y) / Decimal(1000)
        # Adopt Decimal module for precise calculations.
        # Conversion of micrometres to millimetres.

        self.polygon_count = Decimal(polygon_count)
        self.md5sum = md5sum

        self.area_width = self.upper_right_x - self.lower_left_x
        self.area_length = self.upper_right_y - self.lower_left_y
        self.area = self.area_length * self.area_width
        self.density = self.polygon_count / self.area
        # Calculate length, width, area and density.


class Library:
    """This is the Library class that is used to store and sort all instances of Design.

    Attributes:
        design_list: The list used to store Design instances.
    """

    def __init__(self) -> None:
        """Initialise the Library object and create an empty storage list."""
        self.design_list = []

    def add_design(self, design_object: Design) -> None:
        """Add instances of Design to the list: design_list.

        args:
            design_object: Design instances to be added.
        """
        self.design_list.append(design_object)

    def print_reverse_by_density(self) -> None:
        """Prints the name attribute of Design instances in reverse order of instances.

            Internal calculations are done using exact Decimal types,
            and the output is rounded to a more aesthetically pleasing output.
            The name is not recommended to be more than 15 characters
            otherwise it will affect the beautiful output.
        """

        reversed_list = sorted(self.design_list, key=lambda design_lambda: design_lambda.density, reverse=True)
        # Sort by density in reverse order.

        print("{0:15} Density (polygons per mm^2)".format("Name"))
        for design in reversed_list:
            print("{0:15} {1:>15}".format(design.name, design.density.quantize(Decimal("0.00000"))))
            # print(design.name, design.density.quantize(Decimal("0.00000")), sep="\t")
            # Print content.

    @classmethod
    def print_reverse_by_density_class_method(cls, library_object) -> None:
        """Prints the name attribute of Design instances in reverse order of instances.

        Internal calculations are done using exact Decimal types,
        and the output is rounded to a more aesthetically pleasing output.
        The name is not recommended to be more than 15 characters
        otherwise it will affect the beautiful output.

        args:
        library_object: Library instances as storage containers.
        """

        reversed_list = sorted(library_object.design_list, key=lambda design_lambda: design_lambda.density, reverse=True)
        # Sort by density in reverse order.

        print("{0:15} Density".format("Name"))
        for design in reversed_list:
            print("{0:15} {1:>15}".format(design.name, design.density.quantize(Decimal("0.00000"))))
            # print(design.name, design.density.quantize(Decimal("0.00000")), sep="\t")
            # Print content.


class ReadDataIter:
    """Creating an iterable text reading iterator.

    In order to avoid the memory consumption caused by reading a large testdata.txt file at once,
    an iterable class is created.

    Attributes:
        file_pointer: File pointer to an open file.
    """
    def __init__(self, path: str) -> None:
        """Initialising an iterable object.

        path: Path of testdata.txt file.
        """
        self.file_pointer = open(path, "r")

    def __iter__(self) -> iter:
        """Iter methods for iterable objects."""
        return self

    def __next__(self) -> str:
        """Next method for iterable objects.

        returns: Returns a line of string data from testdata.txt.

        raise:End Iterator Flag.
        """
        line = self.file_pointer.readline()
        # Read a line of text data (ending in \n).

        if line == "":
            self.file_pointer.close()
            raise StopIteration()
            # End Iteration.
        else:
            return line
            # Returns the contents of a line as a string.


def store_design_objects(library_object: Library, path: str = "./testdata.txt") -> None:
    """Read the data in testdata.txt and store it in an instance of Library.

    Note that the process of splitting a string first extracts a line of data,
    and subsequently splits a line of data, taking the default split method (by space or \t or \n)

    args:
        library_objects: Library instances as storage containers.
        path: Path to testdata.txt, default is testdata.txt in current directory.
    """
    for design in ReadDataIter(path):
        if design == "name	lower left x (um)	lower left y (um)	" \
                     "upper right x (um)	upper right y (um)	polygon " \
                     "count	md5sum\n" or design == "\n":
            continue
            # Skip useless information.
        else:
            list_of_design = design.split()
            # String splitting, split by space or \t, \n.

            library_object.add_design(Design(*list_of_design))
            # Design object added to Library instance.


if __name__ == '__main__':
    library = Library()
    # Creating Library Object.
    try:
        store_design_objects(library, path="testdata.txt")
        # Read and store Design objects.
    except FileNotFoundError:
        print("The testdata.txt file does not exist, please place the testdata.txt file in your working directory.")
        exit(1)
    except TypeError:
        print("Please check the format of the testdata.txt file")
        exit(1)
    print("Here are the Designs sorted by density from largest to smallest:")
    library.print_reverse_by_density()
    # Print names in reverse density order
