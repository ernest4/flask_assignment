from flask import render_template

from flaskSysInfo import app
from sysinfo import sysinfo

@app.route('/')
def index():
    app.logger.warning('sample message')
    
    returnDict = {}
    returnDict['sysinfo'] = sysinfo.get_platform_info()
    return render_template('index.html', **returnDict)
