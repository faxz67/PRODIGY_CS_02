import argparse
from PIL import Image

def process_image(input_path, output_path, key=42):
    """
    Encrypts or decrypts an image using XOR operation.
    """
    try:
        img = Image.open(input_path)
        img = img.convert('RGB')
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # XOR encryption/decryption
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        print(f"[✓] Image saved to '{output_path}'")
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="PixelCrypt: Image Encryptor/Decryptor")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Operation mode")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to save output image")
    parser.add_argument("--key", type=int, default=42, help="Encryption/Decryption key (default: 42)")

    args = parser.parse_args()

    print(f"[~] {args.mode.capitalize()}ing image...")
    process_image(args.input, args.output, args.key)

if __name__ == "__main__":
    main()
