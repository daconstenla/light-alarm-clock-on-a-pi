from flask import Blueprint
from controllers.AlarmController import index, show

alarms_blueprint = Blueprint('alarms_blueprint', __name__)

alarms_blueprint.route('/', methods=['GET'])(index)
alarms_blueprint.route('/<int:alarmId>', methods=['GET'])(show)
# alarms_blueprint.route('/create', methods=['POST'])(store)
# alarms_blueprint.route('/<int:alarmId>/edit', methods=['POST'])(update)
# alarms_blueprint.route('/<int:alarmId>', methods=['DELETE'])(destroy)