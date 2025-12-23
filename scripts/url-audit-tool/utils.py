#!/usr/bin/env python3
"""
Utility functions for URL Audit Tool
"""

import re
from typing import List, Dict, Optional
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """Check if a string is a valid URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def clean_filename(filename: str) -> str:
    """Clean filename for safe file operations"""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove multiple underscores
    filename = re.sub(r'_+', '_', filename)
    # Remove leading/trailing underscores
    filename = filename.strip('_')
    return filename

def extract_domain_from_url(url: str) -> Optional[str]:
    """Extract domain from URL"""
    try:
        parsed = urlparse(url)
        return parsed.netloc.lower()
    except:
        return None

def categorize_url_type(url: str) -> str:
    """Categorize URL by type"""
    if not url:
        return 'empty'
    
    if url.startswith(('http://', 'https://')):
        return 'absolute'
    elif url.startswith('//'):
        return 'protocol_relative'
    elif url.startswith('/'):
        return 'absolute_path'
    elif url.startswith('#'):
        return 'fragment'
    elif url.startswith('mailto:'):
        return 'email'
    elif url.startswith('tel:'):
        return 'phone'
    elif '{{' in url and '}}' in url:
        return 'template_variable'
    else:
        return 'relative'

def is_image_url(url: str) -> bool:
    """Check if URL points to an image"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.ico'}
    parsed = urlparse(url)
    path = parsed.path.lower()
    return any(path.endswith(ext) for ext in image_extensions)

def get_file_extension_from_url(url: str) -> str:
    """Get file extension from URL"""
    try:
        parsed = urlparse(url)
        path = parsed.path
        if '.' in path:
            return path.split('.')[-1].lower()
        return ''
    except:
        return ''

def normalize_url(url: str) -> str:
    """Normalize URL for comparison"""
    # Remove trailing slash (except for root)
    if url.endswith('/') and url != '/' and not url.startswith(('http://', 'https://')):
        url = url[:-1]
    
    # Convert to lowercase
    url = url.lower()
    
    return url

def group_urls_by_similarity(urls: List[str], threshold: float = 0.8) -> Dict[str, List[str]]:
    """Group URLs by similarity (basic implementation)"""
    from difflib import SequenceMatcher
    
    groups = {}
    processed = set()
    
    for i, url1 in enumerate(urls):
        if url1 in processed:
            continue
            
        group = [url1]
        processed.add(url1)
        
        for j, url2 in enumerate(urls[i+1:], i+1):
            if url2 in processed:
                continue
                
            similarity = SequenceMatcher(None, url1, url2).ratio()
            if similarity >= threshold:
                group.append(url2)
                processed.add(url2)
        
        if len(group) > 1:
            groups[f"group_{len(groups)}"] = group
    
    return groups

def format_file_size(size_bytes: Optional[int]) -> str:
    """Format file size in human readable format"""
    if size_bytes is None:
        return "Unknown"
    
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def format_duration(seconds: float) -> str:
    """Format duration in human readable format"""
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}m"
    else:
        hours = seconds / 3600
        return f"{hours:.1f}h"

def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate string to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length-len(suffix)] + suffix
