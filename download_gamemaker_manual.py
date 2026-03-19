#!/usr/bin/env python3
"""
Download the entire GameMaker manual from manual.gamemaker.io
"""

import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
from pathlib import Path
import time

class LinkExtractor(HTMLParser):
    """Extract all links and resource URLs from HTML"""
    def __init__(self):
        super().__init__()
        self.links = set()
        self.resources = set()
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'a' and 'href' in attrs_dict:
            self.links.add(attrs_dict['href'])
        elif tag == 'link' and 'href' in attrs_dict:
            self.resources.add(attrs_dict['href'])
        elif tag == 'script' and 'src' in attrs_dict:
            self.resources.add(attrs_dict['src'])
        elif tag == 'img' and 'src' in attrs_dict:
            self.resources.add(attrs_dict['src'])

class GameMakerDownloader:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url.rstrip('/')
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Parse the base domain
        parsed = urlparse(base_url)
        self.base_domain = f"{parsed.scheme}://{parsed.netloc}"
        self.base_path = parsed.path.rstrip('/')
        
        self.downloaded = set()
        self.failed = set()
        self.session = urllib.request.Request
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def is_valid_url(self, url):
        """Check if URL belongs to the manual site"""
        url = url.split('#')[0]  # Remove fragment
        if url.startswith('/'):
            return True
        if url.startswith('http'):
            return url.startswith(self.base_domain)
        return True
    
    def normalize_url(self, url, base_url):
        """Normalize URL relative to base"""
        if url.startswith('#') or url == '':
            return None
        if url.startswith('//'):
            return 'https:' + url
        return urljoin(base_url, url)
    
    def get_file_path(self, url):
        """Convert URL to file path"""
        parsed = urlparse(url)
        path = parsed.path.lstrip('/')
        
        if not path or path.endswith('/'):
            path = os.path.join(path, 'index.html')
        
        return self.output_dir / path
    
    def download_file(self, url, is_html=False):
        """Download a single file"""
        if url in self.downloaded:
            return True
        
        if not self.is_valid_url(url):
            return False
        
        url = self.normalize_url(url, self.base_url)
        if not url:
            return False
        
        try:
            file_path = self.get_file_path(url)
            
            # Skip if already downloaded
            if file_path.exists() and file_path.stat().st_size > 0:
                self.downloaded.add(url)
                return True
            
            # Create parent directories
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"Downloading: {url}")
            
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read()
                
                with open(file_path, 'wb') as f:
                    f.write(content)
            
            self.downloaded.add(url)
            
            # Extract links from HTML files
            if is_html:
                try:
                    text = content.decode('utf-8', errors='ignore')
                    parser = LinkExtractor()
                    parser.feed(text)
                    
                    # Download linked pages
                    for link in parser.links:
                        link_url = self.normalize_url(link, url)
                        if link_url and self.is_valid_url(link_url):
                            link_url = link_url.split('#')[0]  # Remove fragment
                            if link_url not in self.downloaded:
                                self.download_file(link_url, is_html=True)
                    
                    # Download resources
                    for resource in parser.resources:
                        res_url = self.normalize_url(resource, url)
                        if res_url and self.is_valid_url(res_url):
                            if res_url not in self.downloaded:
                                self.download_file(res_url, is_html=False)
                except Exception as e:
                    print(f"  Error parsing links: {e}")
            
            time.sleep(0.1)  # Be nice to the server
            return True
            
        except urllib.error.HTTPError as e:
            print(f"  HTTP Error {e.code}: {url}")
            self.failed.add(url)
            return False
        except Exception as e:
            print(f"  Error: {e}")
            self.failed.add(url)
            return False
    
    def download_all(self, start_url):
        """Start the download process"""
        print(f"Starting download from: {start_url}")
        print(f"Saving to: {self.output_dir}")
        print()
        
        self.download_file(start_url, is_html=True)
        
        print()
        print(f"Download complete!")
        print(f"Downloaded: {len(self.downloaded)} files")
        print(f"Failed: {len(self.failed)} files")
        
        if self.failed:
            print("\nFailed downloads:")
            for url in list(self.failed)[:10]:
                print(f"  - {url}")


def main():
    # Configuration
    base_url = "https://manual.gamemaker.io/monthly/en/"
    start_url = "https://manual.gamemaker.io/monthly/en/#t=Content.htm"
    output_dir = "gml"
    
    # Create downloader and start
    downloader = GameMakerDownloader(base_url, output_dir)
    downloader.download_all(start_url)


if __name__ == "__main__":
    main()
