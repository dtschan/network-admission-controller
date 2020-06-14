#!/usr/bin/env python3

import json
import os

from flask import Flask, jsonify, request

application = Flask(__name__)


@application.route("/validate", methods=["POST"])
def validate():
    allowed = True
    print(json.dumps(request.json))

    return jsonify(
        {
            "response": {
                "allowed": allowed,
                "uid": request.json["request"]["uid"],
                "status": {"message": "env keys are prohibited"},
            }
        }
    )


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
