from threading import Thread
import cv2
from videoPlayer.Queue import Queue

class VideoPlayer(object):
    def __init__(self, video_name):
        self.video_name = video_name
        self.frame_count = self.get_frame_count(video_name)
        # Queues
        self.producerQueue = Queue()
        self.consumerQueue = Queue()

    def get_frame_count(self, video_name):
        size = cv2.VideoCapture(video_name).get(cv2.CAP_PROP_FRAME_COUNT)
        return int(size)

    def start(self):
        #creating threads for extracting, conveting, and displaying
        Thread(target=self.extract_frame).start()
        Thread(target=self.convert_to_grayscale).start()
        Thread(target=self.display).start()

    def extract_frame(self):
        # open the video clip
        vid = cv2.VideoCapture(self.video_name)


        while reading:
            # Frames to producer
            self.producerQueue.put(image)
            reading, image = vid.read()

    def convert_to_grayscale(self):
        count = 0
        while count < self.frame_count:
            gray_frame = cv2.cvtColor(self.producerQueue.get(), cv2.COLOR_BGR2GRAY)
            count += 1

            # Add Frame to consumer
            self.consumerQueue.put(gray_frame)

    def display(self):
        while self.consumerQueue:
            #retrieve frame from consumer
            frame = self.consumerQueue.get()
            # Wait for 42 ms and check if the user wants to quit
            cv2.imshow("Video", frame)
            if cv2.waitKey(42) and 0xFF == ord("q") or self.consumerQueue.empty():
                break
        cv2.destroyAllWindows()
