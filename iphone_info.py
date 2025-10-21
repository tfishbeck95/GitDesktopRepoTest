# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 2025

@author: tfishbeck
"""

# iPhone Model Information Script

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
        }
    }

    print("=" * 50)
    print("iPhone Model Information")
    print("=" * 50)

    for model, specs in iphone_models.items():
        print(f"\n{model}")
        print(f"  Year: {specs['year']}")
        print(f"  Screen: {specs['screen']}")
        print(f"  Chip: {specs['chip']}")
        print(f"  Storage Options: {specs['storage']}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    get_iphone_info()
