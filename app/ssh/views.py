from flask import render_template,request,jsonify
from flask_login import login_required
from ..models import VmMachine
from . import ssh
from app import db
from fabric.api import run,env,execute
import sshfunc
import os
@ssh.route('/ssh/connect/<int:id>', methods=['GET', 'POST'])
@login_required
def conection(id):
   machine = VmMachine.query.get_or_404(id)
   programme = db.engine.execute("SELECT * FROM programme WHERE NOT name='solife';")
   return render_template('ssh/home.html',machine=machine, program=programme )
@ssh.route('/ssh/execute', methods=['GET', 'POST'])
@login_required
def executescript():
   id = request.json['id']
   print (request.json)
   programme = request.json['program']
   folder = request.json['folder']
   oracle = request.json['oracle']
   machine = VmMachine.query.get_or_404(id)
   env.host_string = machine.rootName + '@' + machine.ipAddress
   env.password = machine.passwordRoot_hs
   if(machine.os=='windows'):
      for p in programme:
         if (p['name'] == 'Oracle'):
            sshfunc.installOracleWN(machine)
         if (p['name'] == 'Java'):
            sshfunc.installJavaWN(machine)
         if (p['name'] == 'Jboss'):
            sshfunc.installJbossWN(machine)
   else:
      for p in programme :
         if(p['name']=='Oracle'):
          execute(sshfunc.installOracleLX)
         if(p['name']=='Java'):
          execute(sshfunc.installJavaLX)
         if(p['name'] == 'Jboss'):
          execute(sshfunc.installJbossLX)

   return jsonify(status='OK', message='updated successfully')


@ssh.route('/ssh/solife', methods=['GET', 'POST'])
@login_required
def installsolife():
   id = request.json['id']
   print (request.json)
   programme = request.json['solife']
   machine = VmMachine.query.get_or_404(id)
   return jsonify(status='ok', message='database action successfully')
@ssh.route('/ssh/dbase', methods=['GET', 'POST'])
@login_required
def dbaction():
   #test = TestTwo()
   #test.runtest()
   id = request.json['id']
   print (request.json)
   dump=request.json['db']
   machine = VmMachine.query.get_or_404(5)
   env.host_string = machine.userName + '@' + machine.ipAddress
   env.password = machine.password_hs
   execute(sshfunc.datamaniplinux, dump)
   return jsonify(status='ok',message='database action successfully')
@ssh.route('/ssh/metric', methods=['GET', 'POST'])
@login_required
def installread():
   id = request.json['id']
   print (request.json)
   machine = VmMachine.query.get_or_404(id)
   env.host_string = machine.userName + '@' + machine.ipAddress
   env.password = machine.password_hs
   if (machine.os == 'linux'):
      rsp = sshfunc.getMetricLinux(machine)
   else:
      rsp = sshfunc.getMetricWM(machine)
   return jsonify(status='ok', message='database action successfully',response=rsp)





