#!/usr/bin/env pytho3
import subprocess
class p():
  def detachattributes(file):
    subprocess.call(['chattr', '-i', file], shell=False)
  def rootonly(file):
    subprocess.call(['chmod', '0640', file], shell=False)
    subprocess.call(['chown', 'root:root', file], shell=False)
  def shadowfile():
    subprocess.call(['chmod', '400', '/etc/shadow'])
  def attatchattributes(file):
    subprocess.call(['chattr', '+i', file], shell=False)
  def recurse(file):
    subprocess.call(['chown','-R', 'root:root', file], shell=False)

def modifyfile(file):
  p.detachattributes(file)
  p.rootonly(file)
  p.attatchattributes(file)

modifyfile('/etc/fstab')
modifyfile('/etc/passwd')
modifyfile('/etc/group')
modifyfile('/etc/sudoers')
p.shadowfile()
p.recurse('/var/log')
subprocess.call(["mkdir", "-p", "/var/adm"], shell=False)
p.recurse('/var/adm')
p.recurse('/var/tmp')
