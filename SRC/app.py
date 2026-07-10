import os
import pandas as pd
from flask import Flask, render_template, send_file

def create_app():

    app = Flask(
        __name__,
        template_folder=".",
        static_folder="assets",
        static_url_path="/assets"
    )

    # ----------------------------
    # HOME PAGE
    # ----------------------------

    @app.route("/")
    @app.route("/index.html")
    def index():
        return render_template("index.html")

    # ----------------------------
    # DATASET PAGE
    # ----------------------------

    @app.route("/dataset")
    @app.route("/dataset.html")
    def dataset():

        dataset_path = os.path.join(
            app.root_path,
            "data",
            "crop_data.xlsx"
        )

        preview = None
        has_file = os.path.exists(dataset_path)

        if has_file:

            try:

                df = pd.read_excel(dataset_path)

                preview = df.head(20).to_dict(
                    orient="records"
                )

            except Exception as e:

                print("Error loading dataset:", e)

        return render_template(
            "dataset.html",
            preview=preview,
            has_file=has_file
        )

    # ----------------------------
    # DOWNLOAD DATASET
    # ----------------------------

    @app.route("/download")
    def download_dataset():

        dataset_path = os.path.join(
            app.root_path,
            "data",
            "crop_data.xlsx"
        )

        if not os.path.exists(dataset_path):

            return (
                "Dataset not found. Please place crop_data.xlsx inside the data folder.",
                404,
            )

        return send_file(
            dataset_path,
            as_attachment=True,
            download_name="crop_data.xlsx"
        )

    # ----------------------------
    # DASHBOARD PAGE
    # ----------------------------

    @app.route("/dashboard")
    @app.route("/dashboard.html")
    def dashboard():
        return render_template("dashboard.html")

    # ----------------------------
    # STORY PAGE
    # ----------------------------

    @app.route("/story")
    @app.route("/story.html")
    def story():
        return render_template("story.html")

    # ----------------------------
    # ABOUT PAGE
    # ----------------------------

    @app.route("/about")
    @app.route("/about.html")
    @app.route("/insights")
    def about():
        return render_template("about.html")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)