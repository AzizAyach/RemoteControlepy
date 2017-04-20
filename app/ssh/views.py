from flask import render_template,request,jsonify
from flask_login import login_required
from ..models import VmMachine
from . import ssh
from app import db
from fabric.api import run,env,execute
from testtwo import TestTwo
import winrm
folder =''
user = ''
sid=''
@ssh.route('/ssh/connect/<int:id>', methods=['GET', 'POST'])
@login_required
def conection(id):
   machine = VmMachine.query.get_or_404(id)
   programme = db.engine.execute("SELECT * FROM programme WHERE NOT name='solife';")
   return render_template('ssh/home.html',machine=machine, program=programme)


def installJava():
   try:
      run('cd '+folder+' && chmod +x install_db_software.sh && ./install_db_software.sh')
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')


def installOracle():
   try:
      run('cd ' + folder + ' && chmod +x install_db_software.sh && ./install_db_software.sh')
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')
def installJboss():
   try:
      run('cd ' + folder + ' && chmod +x install_db_software.sh && ./install_db_software.sh')
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')



def installenvrWindows(machine):
   try:
      s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password))
      r = s.run_ps('& "C:\Scripts\test.ps1" ')
      print (r.std_out)
   except Exception, e:
      print (e)
      print(r.status_code)
      print(r.std_err)

def datamaniplinux(dump):
   imp = 'impdp '+dump['username']+'/'+dump['pass']+'@'\
         +dump['sid']+' directory=DATAPUMP dumpfile='+dump['dumpfile']+'.EXP logfile= imp-'+dump['logfile']\
         +'.log schemas='+dump['schema']+' remap_tablespace='+dump['rempsource']+':'+dump['remptarget']
   exp = 'expdp '+dump['username']+'/'+dump['pass']+'@'+dump['sid']+' schemas='+dump['schema']\
         +' directory=DATAPUMP dumpfile='+dump['dumpfile']+'.EXP logfile='+dump['logfile']+'.log'
   try:
      if(dump['type']=='imp'):
       run(imp)
      elif(dump['type']=='exp'):
       run(exp)
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')
def datamanipwindows(dump):
   imp = 'impdp '+dump['username']+'/'+dump['pass']+'@'\
         +dump['sid']+' directory=DATAPUMP dumpfile='+dump['dumpfile']+'.EXP logfile= imp-'+dump['logfile']\
         +'.log schemas='+dump['schema']+' remap_tablespace='+dump['rempsource']+':'+dump['remptarget']
   exp = 'expdp '+dump['username']+'/'+dump['pass']+'@'+dump['sid']+' schemas='+dump['schema']\
         +' directory=DATAPUMP dumpfile='+dump['dumpfile']+'.EXP logfile='+dump['logfile']+'.log'
   try:
      if(dump['type']=='imp'):
       run(imp)
      elif(dump['type']=='exp'):
       run(exp)
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')

@ssh.route('/ssh/execute', methods=['GET', 'POST'])
@login_required
def executescript():
   id = request.json['id']
   print (request.json)
   programme = request.json['program']
   global folder
   global user
   global sid
   folder = request.json['folder']
   oracle = request.json['oracle']
   user = oracle['user']
   sid = oracle['sid']
   machine = VmMachine.query.get_or_404(id)
   env.host_string = machine.rootName + '@' + machine.ipAddress
   env.password = machine.passwordRoot_hs
   if(machine.os=='windows'):
      installenvrWindows(machine)
   else:
      for p in programme :
         if(p['name']=='Oracle'):
          execute(installOracle)
         if(p['name']=='Java'):
          execute(installJava)
         if(p['name'] == 'Jboss'):
          execute(installJboss)

   return jsonify(status='OK', message='updated successfully')


@ssh.route('/ssh/solife', methods=['GET', 'POST'])
@login_required
def installsolife():
   id = request.json['id']
   print (request.json)
   programme = request.json['solife']
   machine = VmMachine.query.get_or_404(id)
   return True
@ssh.route('/ssh/dbase', methods=['GET', 'POST'])
@login_required
def dbaction():
   #test = TestTwo()
   #test.runtest()
   id = request.json['id']
   print (request.json)
   db=request.json['db']
   machine = VmMachine.query.get_or_404(id)
   env.host_string = machine.rootName + '@' + machine.ipAddress
   env.password = machine.passwordRoot_hs
   execute(datamaniplinux, db)

   return jsonify(status='ok',message='database action successfully')





