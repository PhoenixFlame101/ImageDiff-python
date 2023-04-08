from imagediff import image_diff, image_data
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    src1_path = "static/1.png"
    src2_path = "static/2.png"

    return render_template("index.html",
                           src1=image_data(src1_path).decode('utf-8'),
                           res=image_diff(
                               src1_path, src2_path).decode('utf-8'),
                           src2=image_data(src2_path).decode('utf-8'))


if __name__ == "__main__":
    app.run()
