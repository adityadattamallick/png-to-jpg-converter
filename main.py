from png_to_jpg import png_to_jpg
import os


def main():
    png_file = os.path.join(os.path.dirname(__file__),
                            "test.png")
    png_to_jpg(png_file)


if __name__ == "__main__":
    main()
