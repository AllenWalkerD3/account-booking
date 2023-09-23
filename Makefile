
STAGE=staging
.PHONY: run
run:
	uvicorn app.main:app --reload    

deploy:
	sls deploy --stage ${STAGE}