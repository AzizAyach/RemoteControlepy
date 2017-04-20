import datetime
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import admin
from forms import VmMachineForm,ProgrammeForm,Config_Notif_Form,User_Form,User_Update_Form
from .. import db
from ..models import VmMachine,Programme,ConfigNotification,User

def check_admin():
    if not current_user.is_admin:
        abort(403)
@admin.route('/vmmachines', methods=['GET', 'POST'])
@login_required
def list_machines():
    check_admin()

    machines = VmMachine.query.all()

    return render_template('admin/machines/machines.html',
                           machines=machines, title="machines")
@admin.route('/vmmachine/add', methods=['GET', 'POST'])
@login_required
def add_machine():
    check_admin()
    add_machine = True
    form = VmMachineForm()
    if form.validate_on_submit():
        machine = VmMachine(name=form.name.data,ipAddress=form.ipAddress.data ,userName=form.userName.data,password_hs = form.password_hs.data,
                            rootName=form.rootName.data,passwordRoot_hs=form.passwordRoot_hs.data,os=form.os.data,
                            last_updated=datetime.datetime.now(),ram=form.ram.data,rom=form.rom.data,cpu=form.cpu.data)
        try:
            db.session.add(machine)
            db.session.commit()
            flash('You have successfully added a new machine.')
        except:
            flash('Error: machine name already exists.')
        return redirect(url_for('admin.list_machines'))

    return render_template('admin/machines/machine.html', action="Add",
                           add_machine=add_machine, form=form,
                           title="Add Machine")

@admin.route('/machines/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_machine(id):
    check_admin()
    add_machine = False
    machine = VmMachine.query.get_or_404(id)
    form = VmMachineForm(obj=machine)
    if form.validate_on_submit():
        machine.name = form.name.data
        machine.ipAddress = form.ipAddress.data
        machine.userName = form.userName.data
        machine.password_hs=form.password_hs.data
        machine.rootName = form.rootName.data
        machine.passwordRoot_hs = form.passwordRoot_hs.data
        machine.os = form.os.data
        machine.ram = form.ram.data
        machine.rom = form.rom.data
        machine.cpu = form.cpu.data
        db.session.commit()
        flash('You have successfully edited the machine.')
        return redirect(url_for('admin.list_machines'))

    form.name.data = machine.name
    form.ipAddress.data = machine.ipAddress
    form.userName.data =machine.userName
    form.password_hs.data = machine.password_hs
    form.rootName.data = machine.rootName
    form.passwordRoot_hs.data = machine.passwordRoot_hs
    form.os.data = machine.os
    form.ram.data = machine.ram
    form.rom.data = machine.rom
    form.cpu.data = machine.cpu
    return render_template('admin/machines/machine.html', action="Edit",
                           add_machine=add_machine, form=form,
                           machine=machine, title="Edit Machine")

@admin.route('/machines/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_machine(id):
    check_admin()
    machine = VmMachine.query.get_or_404(id)
    db.session.delete(machine)
    db.session.commit()
    flash('You have successfully deleted the machine.')
    return redirect(url_for('admin.list_machines'))

    return render_template(title="Delete machines")


@admin.route('/programmes', methods=['GET', 'POST'])
@login_required
def list_programmes():
    check_admin()
    programmes = Programme.query.all()

    return render_template('admin/programmes/programmes.html',
                           programmes=programmes, title="programmes")

@admin.route('/programme/add', methods=['GET', 'POST'])
@login_required
def add_programme():
    check_admin()
    add_programme = True
    form = ProgrammeForm()
    if form.validate_on_submit():
        programme = Programme(name=form.name.data,
                                version=form.version.data,link=form.link.data)
        try:
            db.session.add(programme)
            db.session.commit()
            flash('You have successfully added a new programme.')
        except:
            flash('Error: programme name already exists.')
        return redirect(url_for('admin.list_programmes'))

    return render_template('admin/programmes/programme.html', action="Add",
                           add_programme=add_programme, form=form,
                           title="Add Programme")

@admin.route('/programmes/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_programme(id):
    check_admin()
    add_programme = False
    programme = Programme.query.get_or_404(id)
    form = ProgrammeForm(obj=programme)
    if form.validate_on_submit():
        programme.name = form.name.data
        programme.version = form.version.data
        programme.link = form.link.data
        db.session.commit()
        flash('You have successfully edited the programme.')
        return redirect(url_for('admin.list_programmes'))

    form.name.data = programme.name
    form.version.data = programme.version
    form.link.data =programme.link
    return render_template('admin/programmes/programme.html', action="Edit",
                           add_programme=add_programme, form=form,
                           programme=programme, title="Edit Programme")

@admin.route('/programmes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_programme(id):
    check_admin()
    programme = Programme.query.get_or_404(id)
    db.session.delete(programme)
    db.session.commit()
    flash('You have successfully deleted the programme.')
    return redirect(url_for('admin.list_programmes'))

    return render_template(title="Delete programme")

@admin.route('/configs', methods=['GET', 'POST'])
@login_required
def list_configs():
    check_admin()
    configs = ConfigNotification.query.all()

    return render_template('admin/configs/configs.html',
                           configs=configs, title="configs")

@admin.route('/configs/add', methods=['GET', 'POST'])
@login_required
def add_config():
    check_admin()
    add_config = True
    form = Config_Notif_Form()
    if form.validate_on_submit():
        config = ConfigNotification(name=form.name.data,ram=form.ram.data,
                                rom=form.rom.data,cpu=form.cpu.data)
        try:
            db.session.add(config)
            db.session.commit()
            flash('You have successfully added a new config.')
        except:
            flash('Error: config name already exists.')
        return redirect(url_for('admin.list_configs'))

    return render_template('admin/configs/config.html', action="Add",
                           add_config=add_config, form=form,
                           title="Add Config")

@admin.route('/configs/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_config(id):
    check_admin()
    add_config = False
    config = ConfigNotification.query.get_or_404(id)
    form = Config_Notif_Form(obj=config)
    if form.validate_on_submit():
        config.name = form.name.data
        config.ram = form.ram.data
        config.rom = form.rom.data
        config.cpu = form.cpu.data
        db.session.commit()
        flash('You have successfully edited the config.')
        return redirect(url_for('admin.list_configs'))
    form.name.data =config.name
    form.ram.data = config.ram
    form.rom.data = config.rom
    form.cpu.data = config.cpu
    return render_template('admin/configs/config.html', action="Edit",
                           add_config=add_config, form=form,
                           config=config, title="Edit Config")

@admin.route('/configs/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_config(id):
    check_admin()
    config = ConfigNotification.query.get_or_404(id)
    db.session.delete(config)
    db.session.commit()
    flash('You have successfully deleted the config.')
    return redirect(url_for('admin.list_configs'))

    return render_template(title="Delete config")

@admin.route('/users', methods=['GET', 'POST'])
@login_required
def list_users():
    check_admin()
    users = User.query.all()

    return render_template('admin/users/users.html',
                           users=users, title="users")

@admin.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    check_admin()
    add_user = True
    form = User_Form()
    s=form.is_admin.data
    print (form.is_admin.data)
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,first_name=form.first_name.data,last_name=form.last_name.data,
                    password=form.password.data,is_admin=form.is_admin.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You have successfully added a new user.')
        except:
            flash('Error: user name already exists.')
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html', action="Add",
                           add_user=add_user, form=form,
                           title="Add User")

@admin.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    check_admin()
    add_user = False
    user = User.query.get_or_404(id)
    form = User_Update_Form(obj=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.is_admin = form.is_admin.data
        db.session.commit()
        flash('You have successfully edited the user.')
        return redirect(url_for('admin.list_users'))
    form.email.data = user.email
    form.username.data =user.username
    form.first_name.data = user.first_name
    form.last_name.data = user.last_name
    form.is_admin.data =user.is_admin
    return render_template('admin/users/user.html', action="Edit",
                           add_user=add_user, form=form,
                           user=user, title="Edit User")

@admin.route('/users/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    check_admin()
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('You have successfully deleted the user.')
    return redirect(url_for('admin.list_users'))

    return render_template(title="Delete user")



