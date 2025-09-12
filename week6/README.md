# simple_ubuntu_fetcher.py README

## Overview

**simple_ubuntu_fetcher.py** is a Python script inspired by the Ubuntu philosophy of "I am because we are." It allows users to respectfully fetch and organize images from the global internet community, handling errors gracefully and supporting collective sharing and appreciation of digital resources.[1][3]

## Features

- Prompts for a URL containing an image.
- Connects to the internet to download shared resources.
- Creates a directory called `Fetched_Images` if it doesn't exist.
- Extracts a filename from the image URL or generates a unique name.
- Saves the image in binary mode.
- Handles HTTP errors and exceptions gracefully, providing user-friendly messages.

## Ubuntu Principles

- **Community**: Connects to the wider web community to fetch shared resources.
- **Respect**: Handles errors gracefully, respecting connectivity and permissions.
- **Sharing**: Organizes downloaded images for future sharing.
- **Practicality**: Simple, effective solution to a real-world need.

## Installation

1. **Clone or Download the Script**
   - Place `simple_ubuntu_fetcher.py` in your desired directory.

2. **Install the Required Python Library**
   ```
   pip install requests
   ```

## Usage

1. Run the script:
   ```
   python simple_ubuntu_fetcher.py
   ```
2. Enter the URL of an image when prompted.

3. The image will be saved to the `Fetched_Images` directory, using either its original filename or a generated one.

## Example

```
🌅 Ubuntu Image Fetcher - Assignment Solution
'I am because we are' - Connecting communities through shared resources
==================================================
Enter the URL of the image to fetch: https://www.example.com/image.jpg
✅ Success! Image saved as: Fetched_Images/image.jpg
```

## Error Handling

- Connection problems, timeouts, HTTP errors, file system errors, and unexpected issues are all managed respectfully with informative messages for guidance and resilience.

## License

This project is open-source and free to use for community and educational purposes.

## Author

Created as a demonstration of Ubuntu-inspired coding for resource sharing and respectful programming practice.

