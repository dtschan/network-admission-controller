#!/usr/bin/env python3

import json
import os

from flask import Flask, jsonify, request
import traceback

application = Flask(__name__)


@application.route("/validate", methods=["POST"])
def validate():
    allowed = False
    uid = None
    groups = {}
    message = None

    # print(json.dumps(request.json))

    try:
        admission_request = request.json['request']
        uid = admission_request['uid']
        groups = admission_request['userInfo']['groups']

        if 'pitc-tpl' in groups:
            allowed = True
        else:
            username = admission_request['userInfo']['username']
            operation = admission_request['operation'].lower()
            resource = admission_request['resource']['resource']
            message = f"user '{username}' is not allowed to {operation} {resource}"
    except Exception:
        traceback.print_exc()
        message = f"Invalid request: {json.dumps(request.json)}"
        allowed = False

    return jsonify(
        {
            "response": {
                "allowed": allowed,
                "uid": uid,
                "status": {"message": message},
            }
        }
    )


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080)
