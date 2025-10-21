# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 2025

@author: tfishbeck

iPhone Model Information Script - Pythonista Edition
Dynamically detects iPhone information when running on iOS via Pythonista
"""

import platform
import sys
import os

def get_device_info():
    """Get information about the current device (Pythonista-specific)"""
    device_info = {
        "is_pythonista": False,
        "model": "Unknown",
        "ios_version": "Unknown",
        "screen_width": 0,
        "screen_height": 0,
        "screen_scale": 1,
        "total_disk_space": "Unknown",
        "free_disk_space": "Unknown"
    }

    try:
        # Try to import Pythonista-specific modules
        import console
        device_info["is_pythonista"] = True
    except ImportError:
        pass

    try:
        # Try to use objc_util for more detailed iOS info
        from objc_util import ObjCClass

        UIDevice = ObjCClass('UIDevice')
        current_device = UIDevice.currentDevice()

        # Get device model and iOS version
        device_info["model"] = str(current_device.model())
        device_info["ios_version"] = str(current_device.systemVersion())
        device_info["is_pythonista"] = True

        # Get screen scale and dimensions
        UIScreen = ObjCClass('UIScreen')
        main_screen = UIScreen.mainScreen()
        device_info["screen_scale"] = float(main_screen.scale())

        # Get screen bounds (in points, not pixels)
        bounds = main_screen.bounds()
        device_info["screen_width"] = float(bounds.size.width)
        device_info["screen_height"] = float(bounds.size.height)

        # Get disk space info
        NSFileManager = ObjCClass('NSFileManager')
        file_manager = NSFileManager.defaultManager()

        # Get file system attributes
        attrs = file_manager.attributesOfFileSystemForPath_error_('/', None)
        if attrs:
            total_space = attrs.objectForKey_('NSFileSystemSize')
            free_space = attrs.objectForKey_('NSFileSystemFreeSize')

            if total_space:
                device_info["total_disk_space"] = f"{int(total_space) / (1024**3):.1f} GB"
            if free_space:
                device_info["free_disk_space"] = f"{int(free_space) / (1024**3):.1f} GB"

    except ImportError:
        pass
    except Exception as e:
        print(f"Note: Could not get full device info: {e}")

    return device_info

def display_current_device(device_info):
    """Display information about the current device"""
    print("=" * 50)
    print("YOUR DEVICE INFORMATION")
    print("=" * 50)

    if device_info["is_pythonista"]:
        print(f"Running on: Pythonista (iOS)")
        print(f"Device Model: {device_info['model']}")
        print(f"iOS Version: {device_info['ios_version']}")

        if device_info["screen_width"] > 0:
            screen_diagonal = ((device_info["screen_width"]**2 + device_info["screen_height"]**2)**0.5)
            print(f"Screen Size: {device_info['screen_width']:.0f} x {device_info['screen_height']:.0f} points")
            print(f"Screen Scale: {device_info['screen_scale']:.0f}x")

        if device_info["total_disk_space"] != "Unknown":
            print(f"Total Storage: {device_info['total_disk_space']}")
            print(f"Free Storage: {device_info['free_disk_space']}")
    else:
        print(f"Platform: {platform.system()}")
        print(f"Platform Version: {platform.version()}")
        print(f"Python Version: {sys.version.split()[0]}")
        print("\nNote: Running outside Pythonista - iOS-specific features unavailable")

    print("=" * 50 + "\n")

def get_iphone_info():
    """Display information about various iPhone models"""

    iphone_models = {
        "iPhone 15 Pro Max": {
            "year": 2023,
            "screen": "6.7 inches",
            "chip": "A17 Pro",
            "storage": "256GB, 512GB, 1TB"
        },
        "iPhone 15 Pro": {
            "year": 2023,
            "screen": "6.1 inches",
            "chip": "A17 Pro",
            "storage": "128GB, 256GB, 512GB, 1TB"
        },
        "iPhone 15": {
            "year": 2023,
            "screen": "6.1 inches",
            "chip": "A16 Bionic",
            "storage": "128GB, 256GB, 512GB"
        },
        "iPhone 14 Pro": {
            "year": 2022,
            "screen": "6.1 inches",
            "chip": "A16 Bionic",
            "storage": "128GB, 256GB, 512GB, 1TB"
        },
        "iPhone 14": {
            "year": 2022,
            "screen": "6.1 inches",
            "chip": "A15 Bionic",
            "storage": "128GB, 256GB, 512GB"
        },
        "iPhone 13 Pro": {
            "year": 2021,
            "screen": "6.1 inches",
            "chip": "A15 Bionic",
            "storage": "128GB, 256GB, 512GB, 1TB"
        }
    }

    print("=" * 50)
    print("IPHONE MODEL DATABASE")
    print("=" * 50)

    for model, specs in iphone_models.items():
        print(f"\n{model}")
        print(f"  Year: {specs['year']}")
        print(f"  Screen: {specs['screen']}")
        print(f"  Chip: {specs['chip']}")
        print(f"  Storage Options: {specs['storage']}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    # Get and display current device info
    device_info = get_device_info()
    display_current_device(device_info)

    # Display iPhone models database
    get_iphone_info()
