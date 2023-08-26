from flask    import render_template, request
from app      import app
from app.spam import runSpam

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone')
        time = int(request.form.get('time'))
        runSpam(phone, time)
 
    return render_template('pages/sp.html')

@app.route('/rest', methods=['GET'])
def spamS():
    time = 5
    if request.args.get("time"):
        time  = int(request.args["time"])
    if request.args.get("phone"):
        phone = request.args["phone"]
        runSpam(phone, time)
    return f'Spam phone: {phone}'