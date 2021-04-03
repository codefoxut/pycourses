.phony: help

help:
	@echo "I am here"


bootstrap_init:
	python3.9 -m venv myenv/venv_${APP_NAME}
	myenv/venv_${APP_NAME}/bin/pip3 install -U pip setuptools wheel

bootstrap-all:
	@make bootstrap_init APP_NAME=all
	myenv/venv_all/bin/pip3 install -r requirements.txt

bootstrap-motion-detector:
	@make bootstrap_init APP_NAME=motion_detector
	myenv/venv_motion_detector/bin/pip3 install -r build_application/10_mega_projects_course/motion_detector/requirements_md.txt

run_bokeh_jupyter:
	@myenv/venv_bokeh_app/bin/jupyter notebook

