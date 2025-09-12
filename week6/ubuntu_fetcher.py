import requests
import os
import hashlib
from urllib.parse import urlparse
from requests.utils import unquote_header_value

# ========== Ubuntu Principles ==========

def hash_image_bytes(content):
    """Return SHA-256 hex digest of image content for duplication check."""
    return hashlib.sha256(content).hexdigest()

def get_filename_from_headers(headers, url):
    """Extract filename from Content-Disposition, or URL, otherwise generate one."""
    # Try Content-Disposition header
    cd = headers.get("Content-Disposition")
    filename = None
    if cd and "filename=" in cd:
        filename = unquote_header_value(cd.split("filename=")[-1].split(";")[0].strip(" '\""))
    # Fallback: filename from URL path
    if not filename:
        filename = os.path.basename(urlparse(url).path)
    # Final fallback
    if not filename or '.' not in filename:
        filename = "image_" + hashlib.md5(url.encode('utf-8')).hexdigest()[:8] + ".jpg"
    return filename

def is_downloadable(headers):
    """Precaution: Allow only actual image/content downloads within size limits."""
    content_type = headers.get("Content-Type", "")
    if not content_type.startswith("image/"):
        return False, "Not an image (Content-Type: {})".format(content_type)
    content_length = headers.get("Content-Length")
    if content_length and int(content_length) > 10_000_000:  # Example: 10MB limit
        return False, "Image too large (>{} MB)".format(10)
    return True, ""

def sanitize_filename(filename):
    """Removes risky/special characters (simple whitelist approach)."""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()

def main():
    print("🌅 Ubuntu Image Fetcher: Community edition\nConnect and share mindfully with the world.\n")
    url_input = input("Enter image URLs separated by commas or newlines:\n")
    url_list = [u.strip() for u in url_input.replace('\n', ',').split(',') if u.strip()]

    os.makedirs("Fetched_Images", exist_ok=True)

    # Duplicate prevention: Remember content hashes during this run & record for next
    seen_hashes = set()
    hash_file = "Fetched_Images/hashes.txt"
    if os.path.exists(hash_file):
        with open(hash_file, "r") as hf:
            for line in hf:
                seen_hashes.add(line.strip())

    for url in url_list:
        try:
            # HEAD request for headers/precautions
            head = requests.head(url, timeout=10, allow_redirects=True)
            downloadable, reason = is_downloadable(head.headers)
            if not downloadable:
                print(f"✗ Skipped: {url} — {reason}")
                continue

            response = requests.get(url, timeout=10)
            response.raise_for_status()
            img_bytes = response.content

            image_hash = hash_image_bytes(img_bytes)
            if image_hash in seen_hashes:
                print(f"✗ Skipped duplicate: {url}")
                continue

            seen_hashes.add(image_hash)

            # Get a safe filename
            filename = get_filename_from_headers(response.headers, url)
            filename = sanitize_filename(filename)
            filepath = os.path.join("Fetched_Images", filename)

            # Prevent filename collisions
            base, ext = os.path.splitext(filename)
            idx = 1
            while os.path.exists(filepath):
                filepath = os.path.join("Fetched_Images", f"{base}_{idx}{ext}")
                idx += 1

            with open(filepath, 'wb') as f:
                f.write(img_bytes)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection or HTTP error for {url}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error for {url}: {e}")

    # Save updated hashes for future runs
    with open(hash_file, "w") as hf:
        for h in seen_hashes:
            hf.write(h + "\n")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
