# main.py
import os
from producer_consumer import run_producer_consumer

if __name__ == "__main__":
    input_dir = "producer"
    output_dir = "consumer"
    # Create directories if they don't exist
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    run_producer_consumer(input_dir, output_dir)

    converted = len([f for f in os.listdir(output_dir) if f.endswith("-thumbnail.jpg")])
    print(f"[Main] {converted} images converted successfully.")
