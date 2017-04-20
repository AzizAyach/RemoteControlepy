from flask import render_template,redirect,flash,url_for
from flask_login import login_required
import simplejson as json
from ..models import VmMachine
from . import home
from bson import json_util
from forms import Form_Ssh
from flask_login import current_user
from fabric.api import local, run, cd, env, prefix
import winrm
@home.route('/')
def homepage():
    if current_user:
        return redirect('/dashboard')
    else:
     return redirect('/login')
@home.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    machines = VmMachine.query.all()
    form = Form_Ssh()
    cnx=False
    if form.validate_on_submit():
        machine = VmMachine.query.get_or_404(form.id.data)
        cnx = test_connection(machine)
        if(form.password.data==machine.password_hs and cnx):

            return redirect(url_for('ssh.conection',id=machine.id))
        else:
            flash("Invalid Password or host not connect")
            print ("Invalid Password or host not connect")


    else:
      return render_template('home/dashboard.html',
                           machines=machines, title="machines",form=form)
@home.route('/machines/find/<int:id>', methods=['GET', 'POST'])
@login_required
def list_onemachine(id):
    machine =  VmMachine.query.get_or_404(id)
    return  json.dumps(machine,default=json_util.default)

def test_connection(machine):
    if (machine.os == 'windows'):
        try:
            s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password_hs))
            r = s.run_cmd('ipconfig')
            print (r.std_out)
            return True
        except Exception, e:
            print (e)
            r.std_err
            return False
    elif (machine.os == 'linux'):
        try:
            env.host_string = machine.userName + '@' + machine.ipAddress
            env.password = machine.password_hs
            run('ifconfig')
            return True
        except Exception, e:
            print('' + str(e))
            return False
