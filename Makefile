.PHONY: setup generate demo evaluate test clean

setup:
	python3 -m venv .venv
	.venv/bin/python -m pip install -e '.[test]'

generate:
	python3 scripts/generate_sample_data.py

demo: generate
	python3 scripts/run_demo.py

evaluate: generate
	python3 scripts/evaluate_agents.py

test:
	python3 -m pytest -q

clean:
	rm -rf data/generated reports/*.md reports/*.json .pytest_cache
