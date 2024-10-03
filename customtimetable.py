from airflow.plugins_manager import AirflowPlugin
from airflow.timetables.base import Timetable
from flask import Blueprint

# Creating a flask blueprint to integrate the templates and static folder
bp = Blueprint(
    "test_plugin",
    __name__,
    template_folder="templates",  # registers airflow/plugins/templates as a Jinja template folder
    static_folder="static",
    static_url_path="/static/test_plugin",
)


class CustomTimetable(Timetable):
    pass


class WorkdayTimetablePlugin(AirflowPlugin):
    name = "workday_timetable_plugin"
    flask_blueprints = [bp]
    timetables = [CustomTimetable]