This project demonstrates inter-process communication using Python’s multiprocessing module.
A Producer process reads large images from a source folder, creates smaller thumbnails, and pushes them into a Queue.
A Consumer process retrieves these thumbnails from the queue and saves them in a target folder with a -thumbnail.jpg suffix.

Features:
1)Uses multiprocessing.Queue for producer–consumer communication
2)Handles large image files efficiently
3)Creates thumbnails using the Pillow (PIL) library
4)Clean shutdown after all images are processed
5)Reports the total number of successfully converted images
