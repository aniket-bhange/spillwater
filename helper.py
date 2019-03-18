from flask import json, url_for
from bson import json_util
import os

class Helper:
    def sendResponse(data, app):
        return app.response_class(
            response=json_util.dumps(data),
            status=200,
            mimetype='application/json'
        )
    def sendError(error, app):
        return app.response_class(
            response=json_util.dumps(error),
            status=400,
            mimetype='application/json'
        )
    def save_file(file, filename, folder_path="./uploads"):
        file.save(
            os.path.join(folder_path, filename)
        )
        return url_for('upload_file', filename=filename)

