from flask import Flask, flash, request, redirect, url_for, render_template
from helper import Helper
from spill import WaterLevel
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['npy']

@app.route('/api/upload_numpy_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return Helper.sendError({
            'message': "No File Part",
            'success': False
        }, app)
    file = request.files['file']
    if file.filename == '':
        return Helper.sendError({
            'message': "No File Selected",
            'success': False
        }, app)
    if file and allowed_file(file.filename):
        file_path = Helper.save_file(file, file.filename)
        
        spill_obj = WaterLevel()
        file_name = os.path.join('./uploads', file.filename)
        cube = spill_obj.loadNumpyFile(file_name)
        water_unit = spill_obj.getWaterUnit(cube)
        total_unit = spill_obj.getWaterTotalUnit()
        print(cube, water_unit, total_unit)
        q = spill_obj.saveValue({
            'filename': file.filename,
            'filepath': file_name,
        })
        return Helper.sendResponse({
            'message': "File got Uploaded",
            'success': True,
            'totalunit': str(total_unit),
            'waterunit': str(water_unit),
            'filename': file.filename,
            'id': str(q)
        }, app)
    else:
       return Helper.sendError({
            'message': "Wrong File send",
            'success': False
        }, app) 


@app.route('/api/get_all_units', methods=['POST'])
def getall():
    spill_obj = WaterLevel()
    all_value = spill_obj.getAll()
    print(all_value)
    if all_value:
        return Helper.sendResponse({
            'message': "All Units",
            'success': True,
            'units': all_value
        }, app)
    else:
        return Helper.sendError({
            'message': "No rows selected",
            'success': False
        }, app) 


if __name__ == '__main__':
    app.run(debug=True)