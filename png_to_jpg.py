from PIL import Image


def png_to_jpg(png_file_name: str):
    jpg_filename = png_file_name.rsplit(".", 1)[0] + ".jpg"
    png_img = Image.open(png_file_name)
    png_img.save(jpg_filename, "JPEG", quality=100,
                 subsampling=0, optimize=True)

# convert("RGB"): PNG may have transparency (RGBA), but JPEG doesn’t support it, Hence RGB.
# quality=100: Maximum quality for JPEG, increases file size.
# subsampling=0: Prevents chroma subsampling such as preserves color detail, increases size.
# optimize=True: Does Compress efficiently without losing quality.
