from flask    import render_template, request
from app      import app
from app.spam import runSpam

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone')
        runSpam(phone)
 
    return render_template('pages/sp.html')

@app.route('/rest', methods=['GET'])
def spamS():
    if request.args.get("phone"):
        phone = request.args["phone"]
        runSpam(phone)
    return f'Spam phone: {phone}'