#!/usr/bin/env python3
"""
Ubuntu-Inspired Image Fetcher - Assignment Solution
"I am because we are" - Simple, practical, community-focused
"""

import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    """
    Simple Ubuntu-inspired image fetcher following assignment requirements
    """

    # Ubuntu principle: Community - Prompt user for URL
    url = input("Enter the URL of the image to fetch: ").strip()

    try:
        # Ubuntu principle: Community - Connect to the web
        print("Connecting to fetch the shared resource...")
        response = requests.get(url, timeout=30)

        # Ubuntu principle: Respect - Check for HTTP errors
        response.raise_for_status()

        # Ubuntu principle: Sharing - Create directory for organization
        directory = "Fetched_Images"
        os.makedirs(directory, exist_ok=True)

        # Ubuntu principle: Practicality - Generate appropriate filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename in URL, generate one
        if not filename or '.' not in filename:
            # Generate unique filename
            unique_id = str(uuid.uuid4())[:8]
            filename = f"image_{unique_id}.jpg"

        # Clean filename of query parameters
        filename = filename.split('?')[0]
        filepath = os.path.join(directory, filename)

        # Ubuntu principle: Sharing - Save in binary mode for later appreciation
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"✅ Success! Image saved as: {filepath}")
        print(f"📁 Organized in: {directory}/")
        print("🎉 Ready for community sharing and appreciation!")

    except requests.exceptions.RequestException as e:
        # Ubuntu principle: Respect - Handle errors gracefully
        print(f"🌐 Connection challenge: {e}")
        print("Ubuntu wisdom: 'Not all connections succeed, but we try with respect'")

    except IOError as e:
        # Ubuntu principle: Respect - Handle file errors gracefully  
        print(f"💾 File system challenge: {e}")
        print("Ubuntu wisdom: 'Share what you can, when you can'")

    except Exception as e:
        # Ubuntu principle: Respect - Handle unexpected errors gracefully
        print(f"❓ Unexpected challenge: {e}")
        print("Ubuntu wisdom: 'Every problem teaches us something new'")

if __name__ == "__main__":
    print("🌅 Ubuntu Image Fetcher - Assignment Solution")
    print("'I am because we are' - Connecting communities through shared resources")
    print("=" * 50)
    fetch_image()
