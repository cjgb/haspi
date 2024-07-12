from flask import Flask, jsonify

app = Flask(__name__)

state = {
  'summarize': 0,
  'obsidian-email': 0
}

@app.route("/summarize/", methods=["GET"])
def set_summarize():
    """Increments the state value by 1 and returns the updated state."""
    state['summarize'] = +1
    return jsonify(state)

@app.route("/obsidian-email/", methods=["GET"])
def set_obsidian_email():
    """Increments the state value by 1 and returns the updated state."""
    state['obsidian-email'] = +1
    return jsonify(state)

@app.route("/get/", methods=["GET"])
def get_state():
    """Returns the current state value."""
    out = state.copy()

    for key in state:
        state[key] = 0 if state[key] == 0 else state[key] - 1

    return jsonify(out)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8503)