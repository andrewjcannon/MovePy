from flask import Flask, flash, redirect, render_template, request, session, abort
import main
import configparser

app = Flask(__name__)
app.debug=True

@app.route("/", methods=["GET", "POST"])
def index():
    config = configparser.ConfigParser()
    error = ''
    if request.method == "POST":
        p_status = request.form.getlist('my-checkbox')
        if(len(p_status) > 0 and p_status[0] == "stat"):
            p_status = "on";
        else:
            p_status = "off";

        config.read("config.ini")
        config['RULES'] = {}
        print(request.form)
        status = config['STATUS']
        status['status'] = p_status
        
        settings = config['CONFIGURATION']
        for i in settings:
            settings[i] = request.form[i]
        
        rules = config['RULES']
        num = 0
        for item in request.form:
            if item.startswith('ext'):
                num = num + 1

        looper = 1
        while(num > 0 and looper <= num):
            print("run " + str(looper))
            one = request.form["ext" + str(looper)]
            two = request.form["rule" + str(looper)]

            print(one + " " + two)
            rules[one] = two
            looper = looper + 1

        print(len(rules))
        
        with open("config.ini", "w") as configfile:
            config.write(configfile)
            configfile.close()
        
    config.read("config.ini")
    status = config['STATUS']
    settings = config['CONFIGURATION']
    rules = config['RULES']
    ruleslength = len(rules)

    return render_template('index.html', **locals())

@app.route("/log")
def static_from_root():
    content = "file not found"
    with open("log.txt", "r") as f:
        content=f.read()
        f.close()
        
    return render_template("log.html", content=content)
    
if __name__ == "__main__":
    main.worker_function()
    app.run(host='127.0.0.1', port=7259)
