import sys
sys.path.insert(0, "~/jgw/Dokumente/Papenburg")
from query import or_query

from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='...'
)

@app.route("/")
def hello():
	return render_template('search.html') 

@app.route("/search", methods=['POST'])
def search():
	query=request.form["search"]
	relevant_docs = or_query(query)
	return render_template("result.html", results=relevant_docs, previous_query=query)

@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory('assets', path)
	
if __name__ == "__main__":
	app.run()



