import argparse
from pathlib import Path
from PIL import Image

MAX_WIDTH = 1920
MAX_HEIGHT = 1920
JPEG_WEBP_QUALITY = 80
PNG_WEBP_QUALITY = 85

SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png"}

def is_image(file: Path):
    return file.suffix.lower() in SUPPORTED_FORMATS

def resize_if_needed(img: Image.Image):
    w, h = img.size
    if w <= MAX_WIDTH and h <= MAX_HEIGHT:
        return img

    ratio = min(MAX_WIDTH / w, MAX_HEIGHT / h)
    new_size = (int(w * ratio), int(h * ratio))
    return img.resize(new_size, Image.LANCZOS)

def convert_image(src: Path, dst_dir: Path):
    try:
        with Image.open(src) as img:
            has_alpha = img.mode in ("RGBA", "LA") or (
                img.mode == "P" and "transparency" in img.info
            )

            img = img.convert("RGBA") if has_alpha else img.convert("RGB")
            img = resize_if_needed(img)

            dst_file = dst_dir / f"{src.stem}.webp"

            img.save(
                dst_file,
                "WEBP",
                quality=PNG_WEBP_QUALITY if has_alpha else JPEG_WEBP_QUALITY,
                method=6,
                optimize=True
            )

            print(f"✔ {src.name} → WebP")

    except Exception as e:
        print(f"✖ Failed: {src.name} | {e}")

def process_path(path: Path):
    if path.is_file() and is_image(path):
        out_dir = path.parent / f"{path.stem}_webp"
        out_dir.mkdir(exist_ok=True)
        convert_image(path, out_dir)

    elif path.is_dir():
        out_dir = path.parent / f"{path.name}_webp"
        out_dir.mkdir(exist_ok=True)

        images = [f for f in path.iterdir() if f.is_file() and is_image(f)]
        if not images:
            print("⚠ No images found.")
            return

        for img in images:
            convert_image(img, out_dir)

    else:
        print("✖ Invalid path.")

def main():
    parser = argparse.ArgumentParser(description="Smart JPG/PNG → WebP Converter")
    parser.add_argument("-c", "--convert", required=True, help="Image file or directory")
    args = parser.parse_args()

    target = Path(args.convert).resolve()
    if not target.exists():
        print("✖ Path does not exist.")
        return

    process_path(target)
    print("\n✅ Conversion complete.")

if __name__ == "__main__":
    main()
