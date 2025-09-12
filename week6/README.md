# Ubuntu-Inspired Image Fetcher

A respectful, community-focused Python tool for collecting, organizing, and safeguarding images from the web.



## Overview

**Ubuntu-Inspired Image Fetcher** helps you download multiple images from internet sources, organizing them in a mindful and safe way – embodying the Ubuntu philosophy: "I am because we are". It protects your community and system by validating every download, checking for duplicates, and keeping everything organized for easy sharing.

## Features

- Download multiple images by inputting a comma- or newline-separated list of URLs.
- Automatically saves all images to a `Fetched_Images/` directory.
- Checks content type and file size before saving – only safe, valid images are kept.
- Skips duplicate images based on robust SHA-256 content hashing.
- Extracts a filename from HTTP headers or URL; filenames are sanitized and de-duplicated.
- Friendly, Ubuntu-inspired messages and clear reporting for each URL processed.
- All downloads tracked for future duplicate prevention.

## Requirements

- Python 3.6 or higher
- `requests` library (install with `pip install requests`)

## Usage

1. **Save the script** to your local folder.

2. **Install dependencies:**
   ```sh
   pip install requests
   ```

3. **Run the script:**
   ```sh
   python ubuntu_image_fetcher.py
   ```

4. **Paste or type URLs** (comma- or newline-separated) when prompted.

5. **Find your images** in the `Fetched_Images/` directory, free from duplicates and organized for sharing.

## Example

```
🌅 Ubuntu Image Fetcher: Community edition
Connect and share mindfully with the world.

Enter image URLs separated by commas or newlines:
https://example.com/image1.jpg, https://example.com/image2.png

✓ Successfully fetched: image1.jpg
✓ Image saved to Fetched_Images/image1.jpg
✗ Skipped duplicate: https://example.com/image1.jpg
✗ Skipped: https://example.com/not-an-image — Not an image (Content-Type: text/html)
```

## How It Works

- **Community:** Connects ethically to the global web, downloads with user-provided URLs, and provides Ubuntu-style support messages.
- **Respect:** Only saves valid image types, checks for file size limits, and handles all errors gracefully.
- **Sharing:** Organizes and records every download with care, using safe, unique filenames.
- **Safety:** Skips duplicates based on the actual content of each image, not just filenames.

## Notes on Precautions

- Accepts only URLs with image content types.
- Limits download size to prevent misuse or accidental large downloads.
- Sanitizes all filenames and prevents overwriting existing files.
- Stores image hashes in `Fetched_Images/hashes.txt` to prevent future duplicates.

## License

MIT License. Free to use, adapt, and share for educational and community projects.

## Author

Ubuntu-inspired Python project for learning, sharing, and respectful digital community building.

***

For any improvements, suggestions, or Ubuntu wisdom, contributions are welcome!
