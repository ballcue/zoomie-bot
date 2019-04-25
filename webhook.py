from flask import Flask
import cv2

webhook = Flask(__name__)


@webhook.route('/')
def hello():
    return 'Hello World! {}'.format()


if __name__ == '__main__':
    webhook.run()
