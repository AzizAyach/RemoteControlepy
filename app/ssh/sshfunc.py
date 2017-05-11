from flask import jsonify
import os
import winrm
from fabric.api import run,env
def installJavaLX():
   try:
      path = os.path.abspath('script/java.sh')
      str = open(path).read()
      run(str)
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')


def installOracleLX():
   try:
      path = os.path.abspath('script/oracleall.sh')
      str = open(path).read()
      run(str)
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print('' + str(e))
      return jsonify(status='OK', message='updated successfully')


def installJbossLX():
   try:
      path = os.path.abspath('script/jboss.sh')
      str = open(path).read()
      run(str)
      return jsonify(status='OK', message='updated successfully')
   except Exception, e:
      print(str(e))
      return jsonify(status='OK', message='updated successfully')



   #windows install env



def installOracleWN(machine):
       try:
           path = os.path.abspath('script/oracle.ps1')
           str = open(path).read()
           s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password))
           r = s.run_ps(str)
           print (r.std_out)
           return jsonify(status='OK', message='updated successfully')
       except Exception, e:
           print (e)
           print(r.status_code)
           print(r.std_err)
           return jsonify(status='OK', message='updated successfully')

def installJavaWN(machine):
       try:
           path = os.path.abspath('script/java.ps1')
           str = open(path).read()
           s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password))
           r = s.run_ps(str)
           print (r.std_out)
           return jsonify(status='OK', message='updated successfully')
       except Exception, e:
           print (e)
           print(r.status_code)
           print(r.std_err)
           return jsonify(status='OK', message='updated successfully')

def installJbossWN(machine):
       try:
           path = os.path.abspath('script/jboss.ps1')
           str = open(path).read()
           s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password))
           r = s.run_ps(str)
           print (r.std_out)
           return jsonify(status='OK', message='updated successfully')
       except Exception, e:
           print (e)
           print(r.status_code)
           print(r.std_err)
           return jsonify(status='OK', message='updated successfully')


#import and export data

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
def getMetricLinux(machine):
    env.host_string = machine.rootName + '@' + machine.ipAddress
    env.password = machine.passwordRoot_hs
    try:
        path = os.path.abspath('script/cpu.sh')
        str = open(path).read()
        rsp = run(str)
        return rsp
    except Exception, e:
        print(e)
        return 'erreur'
def getMetricWM(machine):
    try:
        path = os.path.abspath('script/cpu.ps1')
        str = open(path).read()
        s = winrm.Session(machine.ipAddress, auth=(machine.userName, machine.password))
        rsp = s.run_ps(str)
        print (rsp.std_out)
        return rsp
    except Exception, e:
        print(e)
        return rsp