#date finished 17.03.21 kam 18.03.21

from flask import Flask, request, render_template
from search_for_flask import do_all

# liiter just for learning, not need now
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address



app = Flask(__name__)
# limiter = Limiter(
#     app,
#     key_func=get_remote_address,
#     default_limits=["200 per day", "50 per hour"]
# )


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
# @limiter.limit("1 per day")
def my_form_post():
    text = request.form['text']
    NUM_TO_SHOW = 9

    if text:
        processed_text = do_all(text, NUM_TO_SHOW)
        print (processed_text)


        @app.context_processor
        def inject_globals():
            return dict(
                processed_text=processed_text,
            )

        return render_template('search_results.html')
