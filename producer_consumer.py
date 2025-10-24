import os
from multiprocessing import Process, Queue
from PIL import Image

"Reads images from input_dir, creates thumbnails, and puts them in the queue."
def producer_task(queue, input_dir):
    count = 0
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(input_dir, filename)
            try:
                with Image.open(filepath) as img:
                    img=img.convert("RGB")
                    img.thumbnail((128, 128))
                    queue.put((filename, img.copy()))  # send name + image
                    count += 1
                    print(f"[Producer] Queued thumbnail for {filename}")
            except Exception as e:
                print(f"[Producer] Error processing {filename}: {e}")

    # Signal that producer is done
    queue.put(None)
    print(f"[Producer] Done. Total {count} images processed.")

"Consumes thumbnail images from the queue and saves them to output_dir."
def consumer_task(queue, output_dir):
    count = 0
    while True:
        item = queue.get()
        if item is None:
            print("[Consumer] Received termination signal.")
            break

        filename, img = item
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_dir, f"{name}-thumbnail.jpg")
        img.save(output_path, "JPEG")
        count += 1

    return count

"""Main entry point to run producer and consumer processes."""
def run_producer_consumer(input_dir, output_dir):
    queue = Queue()

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    producer = Process(target=producer_task, args=(queue, input_dir))
    consumer = Process(target=consumer_task, args=(queue, output_dir))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("[Main] Producer and Consumer finished.")
