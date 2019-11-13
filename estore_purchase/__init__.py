@app.route("/")
def root():
    return render_template{
        "storepage.html"
    }